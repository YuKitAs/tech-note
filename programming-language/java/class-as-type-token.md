# Class as Type Token

`Class` is generic, for example, the type of `String.class` is `Class<String>`. To store and retrieve an instance of arbitrary different types, we can use `Class<T>` as a type token.

The following class is an example for simple implementation of a typesafe container:

```java
public class ItemContainer {
    private final Map<Class<?>, Object> items = new HashMap<>();

    public <T> void putItem(Class<T> type, T instance) {
        items.put(Objects.requireNonNull(type), instance);
    }

    public <T> T getItem(Class<T> type) {
        return type.cast(items.get(type));
    }
}
```

It can be used like:

```java
ItemContainer container = new ItemContainer();
container.putItem(String.class, "Hello Bonbon");
container.putItem(Integer.class, 42);
container.putItem(Class.class, ItemContainer.class);

System.out.println(container.getItem(String.class)); // Hello Bonbon
System.out.println(container.getItem(Integer.class)); // 42
System.out.println(container.getItem(Class.class).getName()); // ItemContainer
```
