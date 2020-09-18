# Standard Functional Interfaces


Definition: a functional interface is an interface that contains only one abstract method (and possibly multiple default methods). They are (and should be) annotated with `@FunctionalInterface`, for example:

```java
@FunctionalInterface
public interface Action {
    void execute();
}
```

Use:

```java
public static void doSomething(Action action) {
    action.execute();
    // do something else
}

public static void main(String[] args) {
    doSomething(() -> {
        System.out.println("Hello world!");
    });
}
```

Since Java 8, there are some useful standard built-in functional interfaces provided in `java.util.function` like `Consumer<T>`, `Supplier<T>`, `Function<T,R>` and `BiFunction<T,U,R>` (see [more](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)).

The six basic functional interfaces are summarized below:

| Interface | Function Signature | Example |
| --------- | --------- | ------- |
| `UnaryOperator<T>` | `T apply(T t)` | `String::toUpperCase` |
| `BinaryOperator<T>` | `T apply(T t1, T t2)` | `BigInteger::add` |
| `Predicate<T>` | `boolean test(T t)` | `Collection::isEmpty` |
| `Function<T,R>` | `R apply(T t)` | `Arrays::asList` |
| `Supplier<T>` | `T get()` | `Instant::now` |
| `Consumer<T>` | `void accept(T t)` | `System.out::println` |
