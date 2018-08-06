# Dockerize Spring Boot App with MySQL

1. specify the configuration in `application.yml` or `application.properties`, for example:

  ```yaml
  spring:
    profiles: production
    jpa:
      database: mysql
      hibernate:
        ddl-auto: none
    datasource:
      url: jdbc:mysql://docker-mysql:3306/test
      username: root
      password: root
  server:
    port: 8080
  ```

2. Run the MySQL image pulled from [DockerHub](https://hub.docker.com/_/mysql/) with corresponding environment configuration:

  ```console
  # docker run --name=docker-mysql --env="MYSQL_ROOT_PASSWORD=root" --env="MYSQL_PASSWORD=root" --env="MYSQL_DATABASE=<db_name>" mysql:5.7.23
  ```

3. In `build.gradle`, specify the `bootJar`:

  ```gradle
  bootJar {
      baseName = 'test-project'
      version = '0.0.1'
  }
  ```

4. Run `./gradlew build` to build a `build/lib/test-project-0.0.1.jar`.

5. Create a simple `Dockerfile`, don't forget to specify the profile:

  ```Dockerfile
  FROM java:8
  VOLUME /tmp
  EXPOSE 8080
  ADD build/libs/test-project-0.0.1.jar test-project-0.0.1.jar
  RUN bash -c 'touch /test-project-0.0.1.jar'
  ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-Dspring.profiles.active=production","-jar","/test-project-0.0.1.jar"]
  ```

6. Build an image from the current project (with `Dockerfile` in the root, otherwise the path should be given as argument):

  ```console
  # docker build -t test-project .
  ```

7. Link two containers:

  ```console
  # docker run -t --name test-project --link docker-mysql:mysql -p 8080:8080 test-project
  ```
