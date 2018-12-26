# Use of Log4j2

1. Exclude the default logging of Spring Boot and add Log4j2 dependency e.g. into `pom.xml` of a Maven project:

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

2. We can use the default configuration file provided by Spring Boot for Log4j2 by specifying it in `application.properties` as follows:

  ```properties
  logging.config=classpath:org/springframework/boot/logging/log4j2/log4j2.xml
  ```

  Or, create a custom configuration file prefixed with `log4j2` (like `log4j2-*.xml`, `log4j2-*.yaml` or `log4j2-*.json`) in `src/main/resources`. Change the path in `applictaion.properties` and define `Properties`, `Appenders` and `Loggers` something like:

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <Configuration status="WARN">
      <Properties>
          <Property name="LOG_PATTERN">%d{yyyy-MM-dd'T'HH:mm:ss.SSSZ} %p %m%n</Property>
      </Properties>

      <Appenders>
          <!-- Console Appender -->
          <Console name="Console" target="SYSTEM_OUT" follow="true">
              <PatternLayout pattern="${sys:LOG_PATTERN}" alwaysWriteExceptions="false"/>
          </Console>
      </Appenders>

      <Loggers>
          <Logger name="org.apache.catalina.startup.DigesterFactory" level="error"/>
          <Logger name="org.apache.catalina.util.LifecycleBase" level="error"/>
          <Logger name="org.apache.coyote.http11.Http11NioProtocol" level="warn"/>
          <logger name="org.apache.sshd.common.util.SecurityUtils" level="warn"/>
          <Logger name="org.apache.tomcat.util.net.NioSelectorPool" level="warn"/>
          <Logger name="org.hibernate.validator.internal.util.Version" level="warn" />
          <logger name="org.springframework.boot.actuate.endpoint.jmx" level="warn"/>
          <Logger name="com.example.project" level="debug" additivity="false">
              <AppenderRef ref="ConsoleAppender" />
          </Logger>
          <Root level="info">
              <AppenderRef ref="Console"/>
          </Root>
      </Loggers>
  </Configuration>
  ```

3. In the class that needs logging, initialize the logger as follows:

  ```java
  private static final Logger logger = LogManager.getLogger(ClassName.class);
  ```

4. Different log levels can be used with `logger.trace()`, `logger.debug()`, `logger.info()`, `logger.warn()`, `logger.error()` and `logger.fatal()`.
