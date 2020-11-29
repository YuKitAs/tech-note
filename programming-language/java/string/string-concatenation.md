# String Concatenation

## `+` operator
Since strings are immutable, the string concatenation operation `+` will always copy two string and create a new String object. Repeatedly concatenating n strings with `+` requires time complexity `O(n^2)`, the performance will get much worse as the number of concatenation operations grows, so it's discouraged to use `+` in a loop in order to save memory and gc time.

## `concat()`

`String::concat()` works similar to `+`. It will potentially cause NullPointerException. when concatenating an empty string, it will just return the original string instead of creating a new object. Therefore, if the string to concatenate could be empty, `concat()` will perform better than using `+`.

## `StringBuilder`

`StringBuilder` can hold an entire string and only requires linear time, it can also be preallocated with an appropriate size instead of the default size, in order to eliminate the need for automatic growth. For concatenation of multiple strings, it's always recommended to use `StringBuilder` initialized with a proper capacity like:

```java
int n = 1000;
StringBuilder sb = new StringBuilder(n);
for (int i = 0; i < n; i++) {
  sb.append("bon");
}

System.out.println(sb.toString());
```

## `StringBuffer`

`StringBuffer` provides the same functionality as `StringBuilder` but it's thread-safe, due to the synchronization overhead it performs slower than `StringBuilder`.

## `String.format()`

`String.format()` will use regex to parse the arguments and `StringBuilder` to create a formatted string. Performance-wise it's worse than the normal string concatenation with `+`, but it improves readability and is convenient for localization.
