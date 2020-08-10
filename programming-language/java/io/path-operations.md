# Path Operations

## Clean up and convert a path

1. `toUri`

  Converts the path to a string that can be opened from a browser, the file doesn't need to exist:

  ```java
  System.out.println(Paths.get("/home/file").toUri());
  ```

  Output: `file:///home/file`

2. `toAbsolutePath`

  Converts the path to an absolute path, the file doesn't need to exist:

  ```java
  System.out.println(Paths.get("/home/./file").toAbsolutePath());
  ```

  Output: `/home/./file`

3. `toRealPath`

  Returns the absolute path of an existing file, resolves symlinks and removes redundant elements in the path, throws `IOException`:

  ```java
  System.out.println(Paths.get("/home/./yukitas").toRealPath());
  ```

  Output: `/home/yukitas`

## Join two paths

1. Passing a partial path to `resolve` appends it to the original path:

  ```java
  System.out.println(Paths.get("/home/foo").resolve("bar"));
  ```

  Output: `/home/foo/bar`

2. Passing an absolute path to `resolve` returns the absolute path, regardless of the original path:

  ```java
  System.out.println(Paths.get("foo").resolve("/home/bar"));
  ```

  Output: `/home/bar`
