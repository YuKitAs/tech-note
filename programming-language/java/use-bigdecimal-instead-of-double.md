# Use BigDecimal Instead of Double

`BigDecimal` fulfills our needs of special precision better than `Double`, when dealing with financial math issues.

It's better to create a `BigDecimal` number using the `String` constructor:

```java
BigDecimal bd = new BigDecimal("4.2");
```

`setScale()` method can be used to set the number of digits after the decimal and specify the rounding mode:

```java
bd.setScale(1, ROUND_MODE);
```
There are 8 rounding modes: `ROUND_CEILING`, `ROUND_UP`, `ROUND_DOWN`, `ROUND_FLOOR`, `ROUND_HALF_UP`, `ROUND_HALF_DOWN`, `ROUND_HALF_EVEN`, `ROUND_UNNECESSARY`. For details refer to [Javadoc](http://docs.oracle.com/javase/7/docs/api/java/math/BigDecimal.html]).

`BigDecimal` numbers are immutable, arithmetic operations can only be done using methods like `add()` and `multiply()`, each returns a new `BigDecimal` value containing the result.
