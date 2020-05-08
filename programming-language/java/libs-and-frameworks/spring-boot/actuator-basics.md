# Actuator Basics

Spring Boot Actuator is used to monitor and manage applications in production. 

Add [`spring-boot-starter-actuator`](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-actuator) dependency to enable the use of actuator endpoints.

`/actuator/info` and `/actuator/health` are exposed by default.

In the property file, we can configure the management port and prefix for management endpoints instead of `/actuator`, for example:

```properties
management.server.port=9000
management.endpoints.web.base-path=/
```

Then we can visit `localhost:9000/info` to get app details and `localhost:9000/health` to check app health.

The `/info` endpoint can be configured like:

```properties
info.app.name=Sample App
info.app.description=This is my sample app
info.app.version=0.0.1
```

Show details for `/health`:

```properties
management.endpoint.health.show-details=always
```

Expose other endpoints:

```properties
management.endpoints.web.exposure.include=env,loggers,...
```

## Reference

* [Spring Boot Actuator: Production-ready Features](https://docs.spring.io/spring-boot/docs/current/reference/html/production-ready-features.html#production-ready-endpoints), Spring Boot Documentation.
