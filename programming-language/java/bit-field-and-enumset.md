# Bit Field and `EnumSet`

The traditional use of bit fields looks like this:

```java
public class Text {
    public static final int BOLD = 1; // 1
    public static final int ITALIC = 1 << 1; // 2
    public static final int UNDERLINE = 1 << 2; // 4

    public void applyStyle(int styles) { ... }
}

text.applyStyle(Text.BOLD | Text.ITALIC);
```

An alternative is `java.util.EnumSet` which represents sets of values drawn from a single enum type, avoids manual bit shifting, provides type safety and better readability.

So the above example can be refactored using `EnumSet` as follows:

```java
public class Text {
    public enum Style {BOLD, ITALIC, UNDERLINE}

    public void applyStyle(Set<Style> styles) { ... }
}

text.applyStyle(EnumSet.of(Text.Style.BOLD, Text.Style.ITALIC));
```
