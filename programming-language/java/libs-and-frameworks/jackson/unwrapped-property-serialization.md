# Unwrapped Property Serialization

An example for the annotation `@JsonUnwrapped`:

```java
public class Person{
    @JsonUnwrapped
    public Name name;
    public int age;

    public static class Name {
        public String firstName;
        public String lastName;
    }
}
```

The serialized `Person` would then look like:

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 30
}
```

The JSON string can be deserialized "wrapping" to `Person` with `ObjectMapper#readValue`.
