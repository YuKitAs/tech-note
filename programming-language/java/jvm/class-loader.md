# Class Loader

The JVM uses a ClassLoader to load Java classes at runtime.

## Architecture

1. Bootstrap class loader:
root class loader written in native code, load Java core API classes in `<JAVA_HOME>/jre/lib`.

2. Extensions class loader:
load code in `<JAVA_HOME>/jre/lib/ext` or other specified extension directory.

3. System class loader:
load application-specific classes in class path.

4. User-defined custom class loaders:
load code dynamically at runtime.

## Algorithm
1. Check if the class is already loaded
2. If class not loaded, request is delegated to the parent class loader
3. If no class returned by the parent class loader, the requested class is searched by the current class loader
4. If no class can be found by the current class loader, `java.lang.ClassNotFoundException` is thrown

## Custom Implementation

The [`java.lang.ClassLoader`](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html) is an object for loading classes based on a specified binary name (e.g. ` "java.security.KeyStore$Builder$FileBuilder$1"`) of the class. It's an abstract class that can be extended with custom implementations.

A typical strategy is:
1. load class: transform the binary name into a file name (e.g. replace `.` with `/`, append `.class`), read the class file by file name from a file system or class repository, return the binary class file data (raw bytecodes for the class)
2. find class: define a `Class` object from the class name and binary data

## Reference

* [Understanding the Java Classloading Mechanism](http://www2.sys-con.com/itsg/virtualcd/java/archives/0808/chaudhri/index.html), Java Developers Journal
