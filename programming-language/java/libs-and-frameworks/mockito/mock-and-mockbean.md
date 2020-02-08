# `@Mock` and `@MockBean`

The `@Mock` annotation comes from the Mockito library:
```java
@Mock
ExampleService service;
```

It's functionally equivalent to:

```java
ExampleService service = Mockito.mock(ExampleService.class);
```

In order to enable Mockito annotations and avoid side effects between tests, either use the `MockitoJUnitRunner` for the test class, or call the following static method before each test execution:

```java
MockitoAnnotations.initMocks(this);
```

The `@MockBean` annotation comes from the `spring-boot-test` library which wraps the Mockito library, so that the mocks can be added to a Spring `ApplicationContext`. The test class should run with the `SpringRunner` instead of the `MockitoJUnitRunner` to use this annotation. If there is more than one bean of the requested type, use `@Qualifier` at field level. Example:

```java
@RunWith(SpringRunner.class)
public class ExampleTests {
    @MockBean
    @Qualifier("example")
    private ExampleService service;
}
```
