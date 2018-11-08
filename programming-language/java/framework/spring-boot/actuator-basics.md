# Actuator Basics

Spring Boot Actuator is used to monitor and manage applications in production. Above all there are two default endpoints `/actuator/info` and `/actuator/health`.

Firstly the `spring-boot-starter-actuator` dependency should be added.

In property file (e.g. `application.properties`), custom address, port and prefix for management endpoint (instead of `/actuator`) can be specified like:

```properties
management.server.port=9000
management.endpoints.web.base-path=/
```

The `/info` endpoint can provide app details if we configure it in the property file like:

```properties
info.app.name=Sample App
info.app.description=This is my sample app
info.app.version=0.0.1
```

Then we can see the responses by calling `localhost:9000/info` and `localhost:9000/health` after starting the app.
