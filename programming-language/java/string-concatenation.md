# String Concatenation

In the modern IDE, when using the string concatenation operator in a loop, it's suggested that we should use `StringBuilder.append()` instead. Compare the following codes repeatedly concatenating n strings with `+=` and `StringBuilder`:

```java
String result = "";
for (int i = 0; i < n; i++) {
  result += "bon";
}

System.out.println(result);
```

```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < n; i++) {
  sb.append("bon");
}

System.out.println(sb.toString());
```

The latter method would run apparently faster. The reason is that strings are immutable, when two strings are concatenated, both strings will be copied. Therefore, using `+=` in the former method results in time complexity `O(n^2)`, the performance will get much worse as the number of loop grows. In the contrary, `StringBuilder` can hold an entire string and only requires linear time, it can also be preallocated with an appropriate size instead of the default size, in order to eliminate the need for automatic growth.
