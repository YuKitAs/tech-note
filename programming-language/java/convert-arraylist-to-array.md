# Convert `ArrayList` to `Array`

To convert an ArrayList to Array, say, for varargs, the recommended way was to pass a typed Array with the size of the original ArrayList like this:

```java
List<String> stringList = new ArrayList<>();
String[] stringArray = stringList.toArray(new String[stringList.size()]);
```

Using `toArray()` without the typed Array, an `Object[]` will be created rather than `String[]`.

Due to performance reason, it's now preferable to use an empty array instead with either of the following ways:

```java
// the first one is suggested by IntelliJ
String[] stringArray = stringList.toArray(new String[0]);
String[] stringArray = stringList.stream().toArray(String[]::new);
```
