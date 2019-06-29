# Spring Data Redis and Redis Template

The [`RedisTemplate`](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/RedisTemplate.html) is a helper class that provides a high-level abstraction for Redis interaction and thus simplifies Redis data access code (without using Redis Repository). Its subclass [`StringRedisTemplate`](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/StringRedisTemplate.html) is used for string intensive operations.

The template class is thread-safe and can be reused across multiple instances.

By default, it's configured to use Java native serialization.

## Reference

* [Working with Objects through RedisTemplate](https://docs.spring.io/spring-data/data-redis/docs/current/reference/html/#redis:template), Spring Data Redis.
