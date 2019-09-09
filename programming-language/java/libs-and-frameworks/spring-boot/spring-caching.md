# Spring Caching

In order to use caching in Spring Boot application, we are supposed to
1. add `@EnableCaching` on the `@SpringBootApplication` class level
2. use `@Cacheable` with a name on the method level to cache the return value

With the following example, we can track whether the response is retrieved from cache:

```java
@SpringBootApplication
@EnableCaching
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}

@Cacheable("messages")
public String getMessage(String name) {
    logger.debug("Getting message");
    return "Hello " + name;
}
```

If no `CacheManager` or `CacheResolver` has been defined as bean, Spring Boot will try to detect the following cache providers:

```
1. Generic
2. JCache (JSR-107) (EhCache 3, Hazelcast, Infinispan, and others)
3. EhCache 2.x
4. Hazelcast
5. Infinispan
6. Couchbase
7. Redis
8. Caffeine
9. Simple
```

## Caching with Redis

If Redis is available, a `RedisCacheManager` will be auto-configured for caching, with cached key `messages::<name>` in this case. The TTL for keys needs to be configured explicitly.

## Caching with Caffeine

Add the following dependencies:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
<dependency>
  <groupId>com.github.ben-manes.caffeine</groupId>
  <artifactId>caffeine</artifactId>
  <version>2.8.0</version>
</dependency>
```

According to the [official docs](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-caching.html#boot-features-caching-provider-caffeine), it's sufficient to configure properties as follows:

```properties
spring.cache.cache-names=cache1,cache2
spring.cache.caffeine.spec=maximumSize=500,expireAfterAccess=600s
```

However, in my test, the application is still trying to use Redis as cache provider, and it's not possible to use `caffeine` as `spring.cache.type`. So I ended up configuring the `CacheManager` explicitly like:

```java
@Configuration
public class CaffeineCacheConfig {
    @Bean
    public CacheManager cacheManager() {
        CaffeineCache messageCache = buildCache("messages", 60);
        SimpleCacheManager manager = new SimpleCacheManager();
        manager.setCaches(Collections.singletonList(messageCache));
        return manager;
    }

    private CaffeineCache buildCache(String name, int secondsToExpire) {
        return new CaffeineCache(name,
                Caffeine.newBuilder().expireAfterAccess(secondsToExpire, TimeUnit.SECONDS).build());
    }
}
```

## Simple Cache

It can be enabled with `spring.cache.type=simple`. This caching strategy doesn't allow time-based eviction. We need to use `@CacheEvict` with cache name to evict an entry from the cache, when a specific method is called, like a method for updating or deleting an entity.


## Reference
* [Spring Boot Features - Caching](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-caching.html)
