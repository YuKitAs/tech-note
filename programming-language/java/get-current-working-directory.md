# Get Current Working Directory

1. The current directory is represented as system property and `user.dir` is where the JVM was invoked.

  ```java
  System.out.println(System.getProperty("user.dir"));
  ```

2. Use `java.nio.file.Paths`:

  ```java
  System.out.println(Paths.get("").toAbsolutePath());
  ```

  which is equivalent to:

  ```java
  System.out.println(FileSystems.getDefault().getPath("").toAbsolutePath());
  ```
