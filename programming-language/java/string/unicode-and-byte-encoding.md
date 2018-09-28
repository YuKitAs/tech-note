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

Here we should notice, the lengths of the character "A" and "C" are both 1 byte (8 bits), while each of the characters "êñü" has a length of 2 bytes (16 bits), so the length of the byte array would be 8 in this case, while the length of the String is 6.

## Reference

* [Byte Encodings and Strings](https://docs.oracle.com/javase/tutorial/i18n/text/string.html), The Java™ Tutorials for JDK 8, Oracle.
