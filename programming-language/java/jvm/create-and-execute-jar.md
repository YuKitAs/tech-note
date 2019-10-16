# Create and Execute JAR

JAR (Java Archive) is a package file format extended from ZIP.

A JAR can contain one or more applications, and an executable JAR file has to contain at least one main class defined in the manifest file as the entry point.

Compile a Java class and create a JAR:

```console
$ javac Main.java
$ jar cvf example.jar Main.class
```

In the JAR, a default `MANIFEST.MF` will be created in the `META_INF` folder with the version info like:

```
Manifest-Version: 1.0
Created-By: 1.8.0_181 (Oracle Corporation)
```

If executing the JAR directly, we will get an error message `no main manifest attribute, in example.jar` because no entry point (main class) is specified in the manifest header.

We can either pass the main class path as an argument to run the non-executable JAR (arguments after the class name are passed to the `main()` method):

```console
$ java -cp example.jar Main
```

Or create a simple `MANIFEST.MF` with the main class:

```console
Main-Class: Main
```

And then create the JAR with the manifest file to make it executable:

```console
$ jar cvmf MANIFEST.MF example.jar Main.class
```
