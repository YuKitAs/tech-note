# Reading Resources

For a project with Maven standard directory layout

```
src/
  main/
    java/
	resources/
  test/
    jave/
	resources/
```

If we want to read a file from the `main/resources` folder, we can use 

```java
URL url = getClass().getResource("explicit/path/to/filename");
File res = new File(url.getPath());
```

Or with the help of `ClassLoader` which considers the location of the filename is the root:

```java
URL url = getClass().getClassLoader().getResource("filename");
File res = new File(url.getPath());
```

If calling from static method, use `ClassName.class` instead of `getClass()`.
