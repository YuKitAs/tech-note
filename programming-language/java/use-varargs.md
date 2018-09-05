# User Varargs

Varargs are short for variable arguments. Varargs methods accept an arbitrary number of parameters of the same type.

There are two rules for varargs:

1. Each method can have only one varargs parameter
2. The varargs paramter must be the last parameter

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

It's recommended because if we only pass a single varargs parameter and when the method is invoked with no parameter, it won't fail at compile time.
