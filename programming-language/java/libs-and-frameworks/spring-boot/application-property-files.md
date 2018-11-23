# Application Property Files

Normally `SpringApplication` loads properties from `application.properties` or `application.yml` file in a [config location](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html#boot-features-external-config-application-property-files), e.g. in `src/main/resources/`, `project-root/config/` `project-root/`, `src/main/java/config/` or `src/main/java/`.

Custom config file names or locations can be defined as Spring environment properties using command-line args like:

```console
$ java -jar sample.jar --spring.config.name=sample-config
$ java -jar sample.jar --spring.config.location=classpath:/custom1.properties,classpath:/custom2.properties
```

If the location is a directory, it should look like `classpath:custom-config/`. These will override the default file names and locations.

Profile-specific properties have a higher priority than application properties and can be defined by following the naming convention `application-{profile}.properties`. We can choose which property to use by specifying active profiles. For example, to load `application-default.properties` and `application-dev.properties` using command-line args like:

```console
$ java -jar sample.jar --spring.profiles.active=default,dev
```

In IntelliJ Ultimate Edition, the active profiles can be specified in the run configuration.

## Reference

* [Externalized Configuration](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html), Spring Boot Documentation.
