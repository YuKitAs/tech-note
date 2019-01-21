# Use Swagger2 and Springfox to Generate API Docs

1. For Maven project, add the following repository and dependencies:

  ```xml
  <repositories>
    <repository>
      <id>jcenter-snapshots</id>
      <name>jcenter</name>
      <url>https://jcenter.bintray.com/</url>
    </repository>
  </repositories>

  <dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
  </dependency>

  <dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
  </dependency>
  ```

2. Create a class with a `Docket` bean and a `UiConfiguration` bean to setup needed configurations for the API docs:

  ```java
  @Configuration
  @EnableSwagger2
  public class ApiDocumentationConfiguration {
      @Bean
      public Docket documentation() {
          return new Docket(DocumentationType.SWAGGER_2).select()
                  .apis(RequestHandlerSelectors.basePackage("com.example.demo"))
                  .paths(PathSelectors.any())
                  .build()
                  .pathMapping("/")
                  .apiInfo(metadata());
      }

      @Bean
      public UiConfiguration uiConfig() {
          return UiConfigurationBuilder.builder().build();
      }

      private ApiInfo metadata() {
          return new ApiInfoBuilder().title("My Test API").description("Some description").version("1.0").build();
      }
  }
  ```

3. Add annotations in the controller class, like:

  ```java
  @ApiOperation(value = "Get user by id", response = User.class)
  @GetMapping("/{user_id}")
  public User getUser(@PathVariable("user_id") UUID userId) {
    // ...
  }
  ```

4. Add annotations in the model class, like:

  ```java
  @ApiModelProperty(notes = "The name of the user", required = true)
  private final String username;
  ```

5. Run the Spring Boot application, visit `/swagger-ui.html` by default to check the generated API docs.

## More reference

* [Springfox Reference Documentation](http://springfox.github.io/springfox/docs/current/#springfox-spring-mvc-and-spring-boot)
