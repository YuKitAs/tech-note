# Actuator Basics

Spring Boot Actuator is used to monitor and manage applications in production. Above all there are two default endpoints `/actuator/info` and `/actuator/health`.

Firstly the [`spring-boot-starter-actuator`](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-actuator) dependency should be added.

In the property file, we can configure the port and prefix for management endpoints instead of `/actuator` like:

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

See details for `/health`:

```properties
management.endpoint.health.show-details=always
```

## Reference

* [Monitoring and Management over HTTP](https://docs.spring.io/spring-boot/docs/current/reference/html/production-ready-monitoring.html), Spring Boot Documentation.
