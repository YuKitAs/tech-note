# String Comparison

`==` is used to test reference equality (the same object).

`equals()` is used to test value equality (the content of the string).

`==` is cheaper than `equals()`.

However, the following output will be `true` (while `false` is expected) because of JVM optimization.

```java
String a = "Hello";
String b = "Hello";

System.out.println(a == b);
```
