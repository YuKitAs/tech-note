# Unicode and Byte Encoding

A *code point* is a value that can be used in a coded character set. In Unicode standard, the code point value for the Latin character A is `U+0041` (hexadecimal value prefixed with `U+`).

The set of characters from `U+0000` to `U+FFFF` are sometimes referred to as the Basic Multilingual Plane (BMP), characters that are in the range `U+10000` to `U+10FFFF` are called supplementary characters.

`UTF-8` is a character encoding defined by the Unicode standard.

In Java, a String object can be converted into a byte array of non-Unicode characters like:

```java
String str = "A" + "\u00ea" + "\u00f1" + "\u00fc" + "C"; // AêñüC
byte[] bytes = str.getBytes();
```

By default, the converted byte array will be in `UTF-8` format. Other encodings can also be specified as parameter of `getBytes()`, which would throw `UnsupportedEncodingException` though.