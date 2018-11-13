# Usage of `Optional`

`Optional<T>` represents an immutable container that can hold either a single non-null `T` reference or nothing. Instead of returning `null` or throwing an exception, we could return `Optional<E>` with a non-null value.

## `Optional` methods

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

`ifPresent()`: if the value inside the `Optional` object is present, takes a `Consumer` function to do something with the value:

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

`orElseGet()`: similar to `orElse()` but returns a default value produced by a `Supplier<T>`:

```java
String str = null;
String value = Optional.ofNullable(str).orElseGet(this::getDefaultValue);
System.out.println(value); // default
```

So the point is to replace `isPresent()` and `get()` with `ifPresent()` or `orElse()`/`orElseGet()`. The example mentioned above can thus be refactored like this:

```java
Optional<String> str = Optional.ofNullable(getNullableString());
str.ifPresent(this::doSomethingWithStr);
```

The `Consumer` function looks like:

```java
void doSomethingWithStr(String str) {
  // ...
}
```

Since Java 9, there is a new method `ifPresentOrElse​()` which takes an extra `Runnable` (takes no parameter and returns void) to execute when the value is not present, like:

```java
str.ifPresentOrElse(this::doSomethingWithStr, this::doSomethingElse);
```

The `Runnable` function looks like:

```java
void doSomethingElse() {
  // ...
}
```

Notice that an empty list is a non-null value, so when implementing something like `CrudRepository`, it's useless to define `Optional<List<String>>` as the return type, because the list value will always be present even if nothing is found.
