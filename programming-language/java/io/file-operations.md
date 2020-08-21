# File Operations

## Moving/Copying file/directory with copy options

Standard copy options: REPLACE_EXISTING, COPY_ATTRIBUTES, ATOMIC_MOVE

```java
Path source = Paths.get("source.txt");
Path target = Paths.get("target.txt");
Files.move(source, target, REPLACE_EXISTING, ATOMIC_MOVE);
Files.copy(source, target, REPLACE_EXISTING, ATOMIC_MOVE, COPY_ATTRIBUTES);
```

## Checking file/directory

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

## Deleting file/directory

```java
Files.delete(file);
Files.deleteIfExists(file); // failing silently if file does not exists
```

## Creating and reading directory

### Creating

```java
Files.createDirectory(Paths.get("foo")); // `mkdir foo`
Files.createDirectories(Paths.get("foo/bar")); // `mkdir -p foo/bar`
Files.createTempDirectory(Paths.get("."), "tmp-"); // create a temporary directory with prefix in a specified directory (by default in `/tmp`)
```

### Listing contents

```java
try (DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get("."))) {
    for (Path file : stream) {
        System.out.println(file.getFileName());
    }
} catch (IOException | DirectoryIteratorException e) {
    e.printStackTrace();
}
```

### Filtering with Glob pattern

```java
DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get("."), "*.{java,class}");
```

## Reference

* [File and File Store Attributes](https://docs.oracle.com/javase/tutorial/essential/io/fileAttr.html), Oracle docs
