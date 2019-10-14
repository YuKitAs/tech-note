# Spring Security

## HTTP Basic Authentication

1. Add Spring Security dependency:

  ```xml
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
  </dependency>
  ```

2. Add basic authentication values in a configuration file like `application.properties`:

  ```properties
  spring.security.auth.username=test
  spring.security.auth.password=test
  ```

3. Create a class to store the properties:

  ```java

  @ConfigurationProperties("spring.security")
  public class SecurityProperties {
      private final Auth auth = new Auth();

      public Auth getAuth() {
          return auth;
      }

      public static class Auth {
          private String username;
          private String password;

          public String getUsername() {
              return username;
          }

          public String getPassword() {
              return password;
          }

          public void setUsername(String username) {
              this.username = username;
          }

          public void setPassword(String password) {
              this.password = password;
          }
      }
  }
  ```

4. Create a configuration class which extends `WebSecurityConfigurerAdapter` from the Spring Security package and inject the property class:

  ```java
  @Configuration
  @EnableConfigurationProperties(SecurityProperties.class)
  public class SecurityConfig extends WebSecurityConfigurerAdapter {
      private final SecurityProperties securityProperties;

      @Autowired
      public SecurityConfig(SecurityProperties securityProperties) {
          this.securityProperties = securityProperties;
      }

      @Override
      protected void configure(HttpSecurity http) throws Exception {
          http.csrf().disable().authorizeRequests().anyRequest().authenticated().and().httpBasic();
      }

      @Autowired
      public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {
          auth.inMemoryAuthentication()
                  .withUser(securityProperties.getAuth().getUsername())
                  .password("{noop}" + securityProperties.getAuth().getPassword())
                  .roles("USER");
      }
  }
  ```

In Spring Security 5, the default `PasswordEncoder` is `DelegatingPasswordEncoder`, which requires [Password Storage Format](https://spring.io/blog/2017/11/01/spring-security-5-0-0-rc1-released#password-storage-format). For plain text password, we have to add `{noop}`.

In Spring Security, either a role-based or an authority-based authorization is required, e.g. `roles("USER", "ADMIN")` or `authorities("READ_PRIVILEGE").`
