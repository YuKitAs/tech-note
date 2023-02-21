# Usage of jEnv

The command line tool `jenv` can be used to set `JAVA_HOME` environment variables for different JDK versions.


Install and configure `jenv` according to the [official tutorial](http://www.jenv.be/).

Add an installed JDK to jenv like:

```console
$ jenv add /usr/lib/jvm/java-1.17.0-openjdk-amd64
openjdk64-17.0.5 added
17.0.5 added
17.0 added
17 added
```

Use `jenv versions` to list all the available JDKs:

```console
$ jenv versions
* system (set by /home/yukitas/.jenv/version)
  17
  17.0
  17.0.5
  openjdk64-17.0.5  
```

Choose a JDK version:

```console
$ jenv global|local|shell 17
```

Show the current JDK version:

```console
$ jenv version
17 (set by /home/yukitas/.jenv/version)
```

Remove a JDK version:

```console
$ jenv remove 11
```
