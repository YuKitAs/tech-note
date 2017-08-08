# Test Exception

With `JUnit 4`, we can add the JUnit annotation to the test case like

```java
@Test(expected = NumberFormatException.class)
public void testMyMethod() {
    /* ... */
}
```

If the expected exception is thrown, the test will pass.

With `AssertJ`, we can use

```java
assertThatThrownBy(() -> myMethod()).isInstanceOf(NumberFormatException.class);
```

in the test case.
