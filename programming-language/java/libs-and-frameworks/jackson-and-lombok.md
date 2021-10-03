# Jackson and Lombok

The following examples show how to use necessary/minimal Lombok annotations for serialization and deserialization with Jackson.

**Versions**:

* JDK 11
* Lombok: 1.18.20
* Jackson Databind: 2.12.5

In order not to add the `@JsonProperty` and `@JsonCreator` annotations manually, we can enable the following Lombok setting in `lombok.config` in the project root:

```
lombok.anyConstructor.addConstructorProperties=true
```

### Class without inheritance

Non-final class:

```java
@Data // shortcut for `@ToString`, `@EqualsAndHashCode`, `@Getter`, `@Setter` and `@RequiredArgsConstructor`; `@Getter` should be sufficient for basic use of Jackson
@AllArgsConstructor // for instantiation
public class Person {
    private String name;
}
```

The generated `Person` class will have an all args constructor as the default constructor for Jackson:

```java
@ConstructorProperties({"name"})
public Person(String name) {
    this.name = name;
}
```

Test:

```java
String serializedPerson = new ObjectMapper().writeValueAsString(new Person("Joe"));
System.out.println(serializedPerson); // {"name":"Joe"}
Person deserializedPerson = new ObjectMapper().readValue(serializedPerson, Person.class);
System.out.println(deserializedPerson); // Person(name=Joe)
```

Final class with `Builder`:

```java
@Value // immutable version of `@Data`, to make class final and all fields private final
@Builder // to generate a builder for setting fields on instantiation
public class Person {
    String name;
}
```

The generated `Person` class will have an all args constructor as above and a builder.

It can be instantiated as follows and the result will be the same as above:

```java
Person person = Person.builder().name("Joe").build();
```

Alternatively, if not enabling the Lombok setting `addConstructorProperties` mentioned above, we can use `@Jacksonized` (since Lombok 1.18.16) together with `@Builder`.

### Class with inheritance

This can be a little complicated, if we want to deserialize the JSON directly to a child class, the child classes must have at least one distinguishable field of different types.

Parent class:

```java
@JsonIgnoreProperties(ignoreUnknown = true) // ignore the fields for child classes
@JsonTypeInfo(use = JsonTypeInfo.Id.DEDUCTION) // not necessary, if the child classes have distinct fields; introduced in Jackson 2.12
@JsonSubTypes({@JsonSubTypes.Type(Child1.class), @JsonSubTypes.Type(Child2.class)}) // all the child classes, will however cause circular dependency
@Data
@NoArgsConstructor // it has to be added here, because the child classes with custom constructors need to have a default constructor
@AllArgsConstructor(access = AccessLevel.PROTECTED) // for instantiation
public class Parent {
    private String name;
}
```

In this way the parent class can also be abstract class or interface.

One child class without using `Builder`:

```java
@Getter
@ToString(callSuper = true) // not calling super() by default, has to be added explicitly if needed
@EqualsAndHashCode(callSuper = true) // not calling super() by default, has to be added explicitly if needed
@NoArgsConstructor // default constructor for Jackson
public class Child1 extends Parent {
   @JsonProperty("some_text") // not necessary, if the property name is the same as the field name, or the object mapper is configured with proper property naming strategy
   private String someText;

   // the constructor has to be written manually, otherwise the all args constructor of the parent won't called by using @AllArgsConstructor in child
   public Child1(String name, String someText) {
       super(name);
       this.someText = someText;
   }
}
```

Another child class with field of different type and using `Builder`:

```java
// same as above
@Getter
@ToString(callSuper = true)
@EqualsAndHashCode(callSuper = true)
@NoArgsConstructor
public class Child2 extends Parent {
    private int num;

    @Builder // the annotation has to be added for the constructor instead of the class, reason as above
    public Child2(String name, int num) {
        super(name);
        this.num = num;
    }
}
```

Test:

```java
Parent child1 = new Child1("Joe", "foo");
String serializedChild1 = new ObjectMapper().writeValueAsString(child1);
System.out.println(serializedChild1); // {"name":"Joe","some_text":"foo"}
System.out.println(new ObjectMapper().readValue(serializedChild1, Child1.class)); // Child1(super=Parent(name=Joe), someText=foo)

Parent child2 = Child2.builder().name("Joe").num(42).build();
String serializedChild2 = new ObjectMapper().writeValueAsString(child2);
System.out.println(serializedChild2); // {"name":"Joe","num":42}
System.out.println(new ObjectMapper().readValue(serializedChild2,  Child2.class)); // Child2(super=Parent(name=Joe), num=42)
```

Note: Jackson always needs a default constructor, no matter no args or all args. But the no args constructor cannot be used when there are non-initialized final fields.

## References
* [Jackson Polymorphic Deserialization](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization), jackson-docs

* [Jackson 2.12 Most Wanted: Deduction-Based Polymorphism](https://cowtowncoder.medium.com/jackson-2-12-most-wanted-1-5-deduction-based-polymorphism-c7fb51db7818)
