# Assertions

In Java, `assert` is a keyword used to define an assert statement, if the condition is false, an `AssertionError` exception will be thrown. However, assertions are not normal validity checks, they are usually used for debugging and are enabled by passing `-ea` or `-enableassertions` as VM option, otherwise they won't take any effect.

Assertions can also be declared with an error message as optional expression like:

```java
assert list != null && list.size() > 0;
assert num >= 0 : "Number is negative";
```
