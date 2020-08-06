# Copy Files

## Byte streams

Low-level I/O, should only be used for the most primitive I/O.

Example:

```java
try (FileInputStream in = new FileInputStream("input.txt"); FileOutputStream out = new FileOutputStream("output.txt")) {
    int c;
    while ((c = in.read()) != -1) {
        out.write(c);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

## Character streams

Character streams are often "wrappers" for byte streams with `FileReader` and `FileWriter` instead of `FileInputStream` and `FileOutputStream`.

`InputStreamReader` and `OutputStreamWriter` are the bridges for decoding/encoding bytes/characters using a specified charset.

```java
try (FileReader in = new FileReader("input.txt");
     FileWriter out = new FileWriter("output.txt")) {
    int c;
    while ((c = in.read()) != -1) {
        out.write(c);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

Unlike byte streams, the int `c` holds a character value in its last 16 bits (2 bytes).

### Read lines

With `BufferedReader` and `PrintWriter`, a file can be read line by line with a line terminator at the end.

```java
try (BufferedReader in = new BufferedReader(new FileReader("input.txt"));
     PrintWriter out = new PrintWriter(new FileWriter("output.txt"))) {
    String line;
    while ((line = in.readLine()) != null) {
        out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

The output line terminator may be different from the input line terminator, according to the current operating system.
