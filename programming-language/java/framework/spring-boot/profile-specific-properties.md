# Profile-specific Properties

By default, `SpringApplication` loads properties from `application.properties` or `application.yml` in a specified directory. The file name and location can be defined as environment properties like:

```console
$ java -jar sample.jar --spring.config.name=sample-project --spring.config.location=classpath:/default.properties
```

In addition, profile-based properties can be defined by following the naming convention `application-{profile}.properties`. Then we can choose which properties to use, for example, to load `application-default.properties` and `application-dev.properties`:

```console
$ java -jar sample.jar --spring.profiles.active=default,dev
```
