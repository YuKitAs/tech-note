# Spring Boot Admin

To use an admin UI for a Spring Boot application.

## Admin Server

1. Create a new Spring Boot project as admin server with the following dependencies:

  ```xml
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>

  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
  </dependency>

  <dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-server</artifactId>
  </dependency>
  ```

2. In `application.properties` of the server project, configure a custom port and credentials, for example:

  ```
  server.port=9090
  spring.security.user.name=admin
  spring.security.user.password=admin
  ```

3. Add `@EnableAdminServer` annotation in the `Application` class:

  ```java
  @SpringBootApplication
  @EnableAdminServer
  public class Application {

  	public static void main(String[] args) {
  		SpringApplication.run(Application.class, args);
  	}

  }
  ```

4. Configure web security. It's important to disable CSRF for some endpoints that will be called by the client project:

  ```java
  @Configuration
  public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
      @Override
      protected void configure(HttpSecurity httpSecurity) throws Exception {
          SavedRequestAwareAuthenticationSuccessHandler successHandler =
                  new SavedRequestAwareAuthenticationSuccessHandler();
          successHandler.setTargetUrlParameter("redirectTo");
          successHandler.setDefaultTargetUrl("/");

          httpSecurity.authorizeRequests()
                  .antMatchers("/assets/**")
                  .permitAll()
                  .antMatchers("/login")
                  .permitAll()
                  .anyRequest()
                  .authenticated()
                  .and()
                  .formLogin()
                  .loginPage("/login")
                  .successHandler(successHandler)
                  .and()
                  .logout()
                  .logoutUrl("/logout")
                  .and()
                  .httpBasic()
                  .and()
                  .csrf()
                  .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
                  .ignoringAntMatchers("/instances", "/actuator/**");
      }
  }
  ```

5. Run the application by `mvn spring-boot:run`, visit `localhost:9090` and login with username `admin` and password `admin.`

## Admin Client

1. Add the following dependency to the application which has to be configured as a client for the admin server:

  ```xml
  <dependency>
      <groupId>de.codecentric</groupId>
      <artifactId>spring-boot-admin-starter-client</artifactId>
      <version>2.2.2</version>
  </dependency>
  ```

2. In `application.properties` add admin server URL and credentials:

  ```
  spring.boot.admin.client.url=http://localhost:9090
  spring.boot.admin.client.username=admin
  spring.boot.admin.client.password=admin
  ```

3. Expose some management endpoints like:

  ```
  management.endpoints.web.exposure.include=health,info,loggers,env,caches,metrics
  management.endpoint.health.show-details=always
  ```

4. Run the application, it will be automatically registered to the admin server.
