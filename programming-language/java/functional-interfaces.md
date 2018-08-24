# Functional Interfaces

Definition: a functional interface is an interface that contains only one abstract method (and possibly multiple default methods). They are annotated with `@FunctionalInterface`.

Since Java 8, there are some useful built-in functional interfaces like `Consumer<T>`, `Supplier<T>`, `Function<T,R>` and `BiFunction<T,U,R>` (see [more](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)). The following examples showed the usages of `Consumer<T>` and `Function<T,R>`.


### `(T) Consumer<T>: void`
It represents an operation that accepts a single input argument and returns no result.

```java
public static void main(String[] args) {
    readInput(Main::switchToUpperCase);
}

static void readInput(Consumer<String> consumer) {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    String input;
    try {
        input = reader.readLine();
    } catch (IOException e) {
        throw new RuntimeException(e);
    }

    consumer.accept(input); // use a Consumer to receive the input as argument and process it

    System.out.println("done");
}

static void switchToUpperCase(String str) {
    System.out.println(str.toUpperCase());
}
```

In the contrary, `void Supplier<T>: T` represents an operation that doesn't need any argument but returns a result.


### `(T) Function<T,R>: R`
It represents a function that accepts one argument and produces a result.

```java
public static void main(String[] args) {
    readInput(Main::mapToUpperCaseString);
}

static void readInput(Function<String, String> function) {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    String input;
    try {
        input = reader.readLine();
    } catch (IOException e) {
        throw new RuntimeException(e);
    }

    System.out.println(function.apply(input)); // use a Function to receive the input as argument, print the return value

    System.out.println("done");
}

private static String mapToUpperCaseString(String str) {
    return str.toUpperCase();
}
```

Likely, `(T,U) BiFunction<T,U,R>: R` represents a function that accepts two arguments and produces a result.
