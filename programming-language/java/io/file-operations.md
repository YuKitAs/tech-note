# File Operations

## Move/Copy file/directory with copy options

Standard copy options: REPLACE_EXISTING, COPY_ATTRIBUTES, ATOMIC_MOVE

```java
Path source = Paths.get("source.txt");
Path target = Paths.get("target.txt");
Files.move(source, target, REPLACE_EXISTING, ATOMIC_MOVE);
Files.copy(source, target, REPLACE_EXISTING, ATOMIC_MOVE, COPY_ATTRIBUTES);
```

## Check file/directory

### Existence

  ```java
  Path file = Paths.get("file.txt");
  Files.exists(Paths.get("file.txt"));
  Files.notExists(Paths.get("file.txt"));
  ```

  If the existence status of the file is unknown/cannot be verified, both methods will return `false`.

### Accessibility

  ```java
  Files.isWritable(file);
  Files.isReadable(file);
  Files.isExecutable(file);
  ```

### Locating the same file (as symbolic links)

  ```java
  Files.isSameFile(p1, p2);
  ```

## Delete file/directory

```java
Files.delete(file);
Files.deleteIfExists(file); // failing silently if file does not exists
```

## Reference

* [File and File Store Attributes](https://docs.oracle.com/javase/tutorial/essential/io/fileAttr.html), Oracle docs
