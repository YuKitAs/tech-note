# `BufferedReader` and `Scanner`

`BufferedReader` and `Scanner` can both be used to read character-based data from a file or console. Their main differences are listed as follows:

1. `BufferedReader` simply reads data stream, while `Scanner` can tokenize and parse data (separating tokens by whitespaces by default).

2. `BufferedReader` has larger buffer (8192 chars) than `Scanner` (1024 chars).

3. `BufferedReader` is synchronized, thus can be used with multi-threads, while `Scanner` is not thread-safe.

4. `BufferedReader` throws `IOException` while `Scanner` hides it.

The following example shows how to use `BufferedReader` to read input from console:

```java
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
String line;
while ((line = reader.readLine()) != null) {
    System.out.println("input: " + line);
}
```

The equivalent way using `Scanner`:

```java
Scanner scanner = new Scanner(System.in);
while (scanner.hasNext()) {
    System.out.println("input: " + scanner.next());
}
```

Using `Scanner` with `BufferedReader` to read file:

```java
Scanner scanner = new Scanner(new BufferedReader(new FileReader("input.txt")));
while (scanner.hasNext()) {
    System.out.println(scanner.next());
}
```
