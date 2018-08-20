# Use Pattern Matcher

To check if a String matches a certain pattern, the following way with a regular expression might be the most intuitive:

```java
static boolean isHexColorCode(String str) {
  return str.matches("[0-9a-fA-F]{6}");
}
```

However, every time we call `String#matches`, an internal Pattern instance will be created. It's advised to cache this Pattern object to make it reusable, in order to improve the performance. So here is the better way:

```java
private static final Pattern HEX_COLOR_CODE = Pattern.compile("[0-9a-fA-F]{6}"); // It's immutable

static boolean isHexColorCode(String str) {
  return HEX_COLOR_CODE.matcher(str).matches();
}
```
