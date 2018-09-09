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

The leading slash indicates the root `main/resources`. `Class.getResource()` can also accept a `filename` which is located relatively to the package of the class.

Another possibility is to use [`ClassLoader`]((https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html) which considers the location of the `filename` is the root:

```java
URL url = getClass().getClassLoader().getResource("filename");
```

If calling from static method, use `ClassName.class` instead of `getClass()`.

When `url` is not null, we can get the file as follows:

```java
File res = new File(url.getPath());
```

## Reading Resources from Jar

However, from a Jar file, the above-mentioned way won't work. We need to use `getResourceAsStream()` to access a resource properly:

```java
InputStream res = getClass().getResourceAsStream("filename");
```
