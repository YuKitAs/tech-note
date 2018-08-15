# Usage of `Optional`

If using `Optional` like this:

```java
Optional<String> str = Optional.ofNullable(getNullableString());
if(str.isPresent()){
    doSomething(str.get());
}
```

It's actually no different from the classic null check `if(str != null)`.

Take a look into `Optional`.

`Optional.empty()`: used to create an empty `Optional` instance with no value, for example:

```java
Optional<String> empty = Optional.empty();
System.out.println(empty.isPresent()); // false
```

`isPresent()`: checks if the value inside the `Optional` object is non-null. Thus `Optional.empty().isPresent()` is always `false`.

`Optional.of()`: sets a non-null object as the value inside an `Optional` object:

```java
String str = "meh";
Optional<String> opt = Optional.of(str);
System.out.println(opt); // Optional[meh]
System.out.println(opt.get()); // meh

String str = null;
Optional<String> opt = Optional.of(str);
System.out.println(opt); // NullPointerException
```

`Optional.ofNullable()`: sets a nullable object as the value inside an `Optional` object:

```java
String str = null;
Optional<String> opt = Optional.ofNullable(str);
System.out.println(opt); // Optional.empty
```

`ifPresent()`: if the value inside the `Optional` object is present, takes a consumer function to do something with the value:

```java
String str = "meh";
Optional<String> opt = Optional.ofNullable(str);
opt.ifPresent(System.out::println); // meh
```

`orElse()`: used to return a default value if the value inside `Optional` object is not present:

```java
String str = null;
String value = Optional.ofNullable(str).orElse("default");
System.out.println(value); // default
```

`orElseGet()`: similar to `orElse()` but returns a default value produced by a supplying function:

```java
String str = null;
String value = Optional.ofNullable(str).orElseGet(this::getDefaultValue);
System.out.println(value); // default
```

So the point is to replace `isPresent()` and `get()` with `ifPresent()` or `orElse()`/`orElseGet()`. Refactor the bad example mentioned above:

```java
Optional<String> str = Optional.ofNullable(getNullableString());
str.ifPresent(this::doSomething);
```
