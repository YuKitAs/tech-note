# Spring Data Redis and Redis Template

The [`RedisTemplate`](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/RedisTemplate.html) is a helper class that provides a high-level abstraction for Redis interaction and thus simplifies Redis data access code (without using Redis Repository). Its subclass [`StringRedisTemplate`](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/StringRedisTemplate.html) is used for string intensive operations.

The template class is thread-safe and can be reused across multiple instances.

By default, it's configured to use Java native serialization.

The template provides operations views like Key Type Operations `HashOperations`, `ListOperations` and Key Bound Operations `BoundHashOperations` that offer interfaces for operations with a certain type or certain key.


## Object Hash Mapping

The following is a Java example for writing an Object to Redis Hash and reading the Object from Hash without enabling `RedisRepository`, in order to gain more control over data interactions.

 First of all, in the `@Configuration` class, add `@Bean` for a chosen `RedisConnectionFactory`, `RedisTemplate<H, V>` and `HashOperations<H, HK, HV>` with consistent types, optionally `RedisCustomConversions` with custom converters and a `HashMapper<Object, byte[], byte[]>` with the custom conversions.

```java
@Bean
public RedisConnectionFactory lettuceConnectionFactory() {
    return new LettuceConnectionFactory(); // the default connection factory, must be explicitly defined.
}

@Bean
public RedisTemplate<String, byte[]> redisTemplate() {
    RedisTemplate<String, byte[]> redisTemplate = new RedisTemplate<>();
    redisTemplate.setConnectionFactory(lettuceConnectionFactory());
    redisTemplate.setKeySerializer(new StringRedisSerializer());

    return redisTemplate;
}

@Bean
public HashOperations<String, byte[], byte[]> hashOperations() {
    return redisTemplate().opsForHash();
}

@Bean
public RedisCustomConversions redisCustomConversions() {
    return new RedisCustomConversions(Arrays.asList(
            new UUIDToBytesConverter(),
            new BytesToUUIDConverter()
    ));
}

@Bean
public HashMapper<Object, byte[], byte[]> objectHashMapper() {
    return new ObjectHashMapper(redisCustomConversions());
}
```

Assuming that the object contains an id of UUID type, and the other fields are all Strings, so we only need to define two converter classes for conversions between `UUID` and `byte[]`. They could look like this:

```java
@WritingConverter
public class UUIDToBytesConverter implements Converter<UUID, byte[]> {
    @Override
    public byte[] convert(final UUID source) {
        return source.toString().getBytes(StandardCharsets.UTF_8);
    }
}

@ReadingConverter
public class BytesToUUIDConverter implements Converter<byte[], UUID> {
    @Override
    public UUID convert(final byte[] source) {
        return UUID.fromString(new String(source, StandardCharsets.UTF_8));
    }
}
```

The object class is nothing special but needs a default empty constructor.

After the configuration, we could simply inject a `HashOperations<String, byte[], byte[]>` and instantialize an `ObjectHashMapper` which is an implementation of `HashMapper<Object, byte[], byte[]>`, just as the example in the official tutorial of Spring Data Redis:

```java
@Autowired
HashOperations<String, byte[], byte[]> hashOperations;
HashMapper<Object, byte[], byte[]> mapper = new ObjectHashMapper();
```
However, since the `HashMapper` is configured as Bean in order to use `RedisCustomConversions`, it can also be autowired.

Saving object:

```java
String key = "obj:" + objId; // a Redis keyspace naming convention
Map<byte[], byte[]> objHash = hashMapper.toHash(obj);
hashOperations.putAll(key, objHash);
```

Reading hash:

```java
Map<byte[], byte[]> entries = hashOperations.entries(key);
MyObject obj = (MyObject) hashMapper.fromHash(entries);
```

For some operations like setting expiry, the `RedisTemplate` should be autowired as well, and it's as simple as one line of code:

```java
redisTemplate.expire(key, 1, TimeUnit.DAYS);
```

## Object to JSON String

```java
redisTemplate.opsForValue().set(key, obj);
Obj obj = redisTemplate.opsForValue().get(key); // nullable
```

## Reference

* [Working with Objects through RedisTemplate](https://docs.spring.io/spring-data/data-redis/docs/current/reference/html/#redis:template), Spring Data Redis.
