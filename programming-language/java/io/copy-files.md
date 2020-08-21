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

## Data streams

Data streams support I/O of primitive data type values as well as Strings. `DataInputStream` and `DataOutputStream` implement `DataInput` and `DataOutput`, and must be constructed as a wrapper for a byte stream.

One drawback of `DataStreams` is that it uses floating point numbers to represent values, the current way is to use `BigDecimal` type with `ObjectStreams`.


## Object streams

Object streams support I/O of objects. `ObjectInputStream` and `ObjectOutputStream` implement `ObjectInput` and `ObjectOutput`, which are subinterfaces of `DataInput` and `DataOutput`.

## File I/O (Featuring NIO.2)

### Buffered streams

```java
Charset charset = StandardCharsets.UTF_8;
try (BufferedReader reader = Files.newBufferedReader(Paths.get("input.txt"),
        charset); BufferedWriter writer = Files.newBufferedWriter(Paths.get("output.txt"), charset)) {
    String line;
    while ((line = reader.readLine()) != null) {
        writer.write(line + "\n");
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### Unbuffered streams

```java
BufferedReader reader = new BufferedReader(
                new InputStreamReader(Files.newInputStream(Paths.get("input.txt"))));
OutputStream out = new BufferedOutputStream(
                Files.newOutputStream(Paths.get("output.txt"), CREATE, APPEND));
```

### Channel I/O

`java.nio.channels.Channel` is designed to provide for bulk data transfers to and from NIO buffers. `FileChannel` is an implementation of `SeekableByteChannel` for reading, writing, mapping, and manipulating a file (from any position).

Reading from a file with `java.nio.ByteBuffer`:

```java
Path file = Paths.get("file.txt");
try (SeekableByteChannel sbc = Files.newByteChannel(file)) {
    ByteBuffer buf = ByteBuffer.allocate(12);

    // Read the bytes with the proper encoding for this platform.
    String encoding = System.getProperty("file.encoding");
    while (sbc.read(buf) > 0) {
        buf.rewind(); // set position to 0 to read from buffer
        System.out.print(Charset.forName(encoding).decode(buf));
        buf.flip(); // set limit to the current position and set position to 0
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

Writing (creating and appending) to a file:

```java
Set<OpenOption> options = new HashSet<>();
options.add(APPEND);
options.add(CREATE);

Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rw-r-----");
FileAttribute<Set<PosixFilePermission>> attr = PosixFilePermissions.asFileAttribute(perms);

String s = "Hello World!";
byte[] data = s.getBytes();
ByteBuffer bb = ByteBuffer.wrap(data);

Path file = Paths.get("file.txt");

try (SeekableByteChannel sbc = Files.newByteChannel(file, options, attr)) {
    sbc.write(bb);
} catch (IOException e) {
    e.printStackTrace();
}
```
