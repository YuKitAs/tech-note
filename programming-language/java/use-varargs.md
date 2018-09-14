# User Varargs

Varargs are short for variable arguments. Varargs methods accept an arbitrary number of parameters of the same type.

There are two rules for varargs:

1. Each method can have only one varargs parameter
2. The varargs parameter must be the last parameter

If we want to pass at least one argument using varargs, the recommended way is to declare the method with the first argument like:

```java
static int min(int firstArg, int... remainingArgs) {
    int min = firstArg;
    for (int arg : remainingArgs) {
        if (arg < min) {
            min = arg;
        }
    }
    return min;
}
```

It's recommended because if we only pass a single varargs parameter and when the method is invoked with no parameter, it wouldn't immediately fail at compile time.

However, it could be unsafe to combine generics and varargs. For example, the generic varargs parameter `List<String>... stringLists` can be stored into a generic array (`Object[] objects = stringLists`), which is illegal, without compiler error. Otherwise, if the method with a varargs parameter of a generic type (e.g. `List<E>`) or parameterized type (e.g. `List<String>`) is ensured to be typesafe, use the `@SafeVarargs` annotation to suppress warnings.
