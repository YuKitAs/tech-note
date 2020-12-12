# Setup Sentry

Sentry is a monitoring and error tracking platform. After created a new project on [sentry.io](https://sentry.io/), we will see a DSN like `https://<public-key>@o0.ingest.sentry.io/0` for the project.

In Spring Boot project, add Sentry dependency:

```xml
<dependency>
  <groupId>io.sentry</groupId>
  <artifactId>sentry-spring-boot-starter</artifactId>
  <version>3.2.0</version>
</dependency>
```

Add DSN into config file:

```
sentry.dsn=https://<public-key>@o0.ingest.sentry.io/0
```

By default, all the unhandled exceptions will be logged on Sentry as project issues. We can also manually capture a caught exception like:

```java
try {
    throw new Exception("test");
} catch (Exception e) {
    Sentry.captureException(e);
}
```
