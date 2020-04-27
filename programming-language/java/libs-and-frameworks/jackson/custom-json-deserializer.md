# Custom Json Deserializer

Create a class for custom deserializer, e.g. to preprocess String properties:

```java
public class CustomStringDeserializer extends JsonDeserializer<String> {
    @Override
    public String deserialize(JsonParser jsonParser, DeserializationContext deserializationContext) {
        // do something and return the processed string
    }
}
```

Add annotation for JSON property to register the deserializer:

```java
@JsonDeserialize(using = CustomStringDeserializer.class)
private String prop;
```

This annotation can also be used on the class level if the deserializer is defined for Object properties.
