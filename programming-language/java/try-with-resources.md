# `try`-with-resources

When reading a resource and writing it to a new one with `FileInputStream` and `FileOutputStream`, the traditional way may look like:

```java
static void copyResource(String src, String dst) throws IOException {
    InputStream in = new FileInputStream(src);
    try {
        OutputStream out = new FileOutputStream(dst);
        try {
            byte[] buf = new byte[BUFFER_SIZE];
            int n;
            while ((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
        } finally {
            out.close();
        }
    } finally {
        in.close();
    }
}
```

However, the exceptions thrown by calling `close` in the `finally` block may obliterate the exceptions thrown from the code inside the `try` block, so it's recommended to use `try`-with-resources statement instead of `try-finally` since Java 7, which will also be auto-suggested by modern IDE. If we accept the suggestions, the above code will be refactored as follows:

```java
static void copyResource(String src, String dst) throws IOException {
    try (InputStream in = new FileInputStream(src)) {
        try (OutputStream out = new FileOutputStream(dst)) {
            byte[] buf = new byte[BUFFER_SIZE];
            int n;
            while ((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
        }
    }
}
```

Because `FileInputStream` and `FileOutputStream` have implemented the interface `AutoClosable`, they will be closed regardless of whether the `try` statement finishes normally or not.

Instead of using nested `try` blocks, multiple resources can be declared in one `try`-with-resources statement separated by semicolon:

```java
static void copyResource(String src, String dst) throws IOException {
    try (InputStream in = new FileInputStream(src); OutputStream out = new FileOutputStream(dst)) {
        byte[] buf = new byte[BUFFER_SIZE];
        int n;
        while ((n = in.read(buf)) >= 0) {
            out.write(buf, 0, n);
        }
    }
}
```
