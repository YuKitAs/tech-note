# Configuration Properties

The following example shows how to define and use custom properties in property file.

Given `application.yml` in one of the default config locations:

```yml
my:
  secrets:
    prop: foo
```

Then we have to define a class with attribute of the same name and getters/setters like:

```java
@Configuration
@ConfigurationProperties(prefix = "my.secrets")
public class DemoProperties {
    private String prop;

    public String getProp() {
        return prop;
    }

    public void setProp(String prop) {
        this.prop = prop;
    }
}
```

A `@Configuration` or `@Component` annotation here is used to make this class as a bean so that we can inject it into any other class with `@Autowired`.


Other ways to read values from propery sources see note [Spring Value Annotation](https://github.com/YuKitAs/tech-note/blob/master/programming-language/java/libs-and-frameworks/spring-boot/spring-value-annotation.md).
