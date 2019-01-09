# Use of Log4j2

1. Exclude the default logging of Spring Boot and add Log4j2 dependency.

  In `pom.xml` of Maven project:

  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <exclusions>
          <exclusion>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-logging</artifactId>
          </exclusion>
      </exclusions>
  </dependency>
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-log4j2</artifactId>
  </dependency>
  ```

  In `build.gradle` of Gradle project:

  ```gradle
  configurations {
    implementation.exclude module: 'spring-boot-starter-logging'
  }

  dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web')
    implementation('org.springframework.boot:spring-boot-starter-log4j2')
  }
  ```

2. We can use the default configuration file provided by Spring Boot for Log4j2 by specifying it in `application.properties` as follows:

  ```properties
  logging.config=classpath:org/springframework/boot/logging/log4j2/log4j2.xml
  ```

  If using the default config file, we can also configure logging levels with format `logging.level.<package.name>=<LEVEL>`. For example:

  ```properties
  logging.level.com.example.project=DEBUG
  ```

  Alternatively, create a custom config file prefixed with `log4j2` (like `log4j2-*.xml`, `log4j2-*.yaml` or `log4j2-*.json`) in `src/main/resources`. Change the path in `applictaion.properties` and define `Properties`, `Appenders` and `Loggers`. An official example of custom `log4j2.xml` can be found [here](https://github.com/spring-projects/spring-boot/blob/v2.1.1.RELEASE/spring-boot-project/spring-boot/src/main/resources/org/springframework/boot/logging/log4j2/log4j2.xml).

3. In the class that needs logging, initialize the logger as follows (import `Logger` and `LogManager` from `org.apache.logging.log4j`):

  ```java
  private static final Logger logger = LogManager.getLogger(ClassName.class);
  ```

4. Different log levels can be used with `logger.trace()`, `logger.debug()`, `logger.info()`, `logger.warn()`, `logger.error()` and `logger.fatal()`. In some cases, it costs too much time to evaluate the info to be logged, to avoid performance impact, we could check the log level before, like:

  ```java
  if (logger.isDebugEnable()) {
    logger.debug("Logging: {}", thisOperationCostsMuchTime());
  }

  ```

  so that it won't be evaluated when this log level isn't enabled.
