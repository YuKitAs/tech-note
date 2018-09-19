# `printf` and `format`

`printf(String format, Object... args)` and `format(String format, Object... args)` are both formatting methods for standard output provided by `java.io.PrintStream` and are equivalent. Basically they are used like this:

```java
System.out.format("The value of the string is %s and the value of the integer is %d%n", s, i);
System.out.printf("The value of the double is %.2f%n", d);
// equivalent to `System.out.println(String.format("...", ...))`
```

Unlike the `printf` in C, the `%n` in Java generates a platform-specific new line character.
