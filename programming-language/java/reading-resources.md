# Reading Resources

For a project with Maven standard directory layout

```
src/
  main/
    java/
	resources/
  test/
    java/
	resources/
```

If we want to read a file from the `main/resources` folder, we can use 

```java
URL url = getClass().getResource("/filename");
```

The leading slash indicates the root `main/resources`. `Class.getResource()` can also accept a `filename` which is located relative to the package of the class.

Another possibility is to use `ClassLoader` which considers the location of the `filename` is the root:

```java
URL url = getClass().getClassLoader().getResource("filename");
```

If calling from static method, use `ClassName.class` instead of `getClass()`.

When `url` is not null, we can get the file as follows:

```java
File res = new File(url.getPath());
```
