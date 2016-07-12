# Spring Context

The following example shows the basic concept of spring dependency injection.

Firstly, add the spring-context dependency of Spring Framework:

  ```xml
  <dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>4.3.1.RELEASE</version>
    </dependency>
  </dependencies>
  ```
  
We will create an interface with `getMessage()` method:

  ```java
  public interface MessageService {
      String getMessage();
  }
  ```
  
Then, create a class which calls the a `getMessage()` method. This class must be annotated with `@Component` annotation to indicate this is an auto scan component:

  ```java
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Component;

  @Component
  public class MessagePrinter {

      final private MessageService service;

      @Autowired
      public MessagePrinter(MessageService service) {
          this.service = service;
      }

      public void printMessage() {
          System.out.println(service.getMessage());
      }
  }
  ```

At last, create a class with `@Configuration` and `@ComponentScan` annotations. The `@Configuration` annotation indicates that this class will be used by JavaConfig as a source of bean definitions. We will declare the `mockMessageService()` method which returns an instance of MessageService as a bean using `@Bean` annotation:

  ```java
  import org.springframework.context.ApplicationContext;
  import org.springframework.context.annotation.*;

  @Configuration
  @ComponentScan
  public class Application {

      @Bean
      public MessageService mockMessageService() {
          return new MessageService() {
              public String getMessage() {
                return "Hello World!";
              }
          };
      }

      public static void main(String[] args) {
          ApplicationContext context = 
              new AnnotationConfigApplicationContext(Application.class);
          MessagePrinter printer = context.getBean(MessagePrinter.class);
          printer.printMessage();
      }
  }
  ```

As shown above, the `MessagePrinter()` class doesn't need to care about the object it depends on. It'll be done by Spring's `ApplicationContext.getBean()`.
