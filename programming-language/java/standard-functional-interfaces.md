# Standard Functional Interfaces

Definition: a functional interface is an interface that contains only one abstract method (and possibly multiple default methods). They are annotated with `@FunctionalInterface`.

Since Java 8, there are some useful standard built-in functional interfaces like `Consumer<T>`, `Supplier<T>`, `Function<T,R>` and `BiFunction<T,U,R>` (see [more](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)).

The six basic functional interfaces are summarized below:

| Interface | Function Signature | Example |
| --------- | --------- | ------- |
| `UnaryOperator<T>` | `T apply(T t)` | `String::toUpperCase` |
| `BinaryOperator<T>` | `T apply(T t1, T t2)` | `BigInteger::add` |
| `Predicate<T>` | `boolean test(T t)` | `Collection::isEmpty` |
| `Function<T,R>` | `R apply(T t)` | `Arrays::asList` |
| `Supplier<T>` | `T get()` | `Instant::now` |
| `Consumer<T>` | `void accept(T t)` | `System.out::println` |

The following example shows the usage of `UnaryOperator<T>`:

```java
public static void main(String[] args) {
    readInput(this::mapString);
}

static void readInput(UnaryOperator<String> operator) {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    String input;
    try {
        input = reader.readLine();
    } catch (IOException e) {
        throw new RuntimeException(e);
    }

    System.out.println(operator.apply(input));
    System.out.println("Done");
}

private static String mapString(String str) {
    return str.toUpperCase();
}
```
