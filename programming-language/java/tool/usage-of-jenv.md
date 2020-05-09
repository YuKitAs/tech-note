# Usage of jEnv

The command line tool `jEnv` can be used to set `JAVA_HOME` environment variables for different JDK versions.


After installed and configured `jEnv` according to the [tutorial](http://www.jenv.be/), use `jenv versions` to list all the available JDKs, like:

```console
$ jenv versions
* system (set by /home/yukitas/.jenv/version)
  oracle64-10.0.2
  oracle64-1.8.0.112
```

Then choose a JDK version:

```console
$ jenv global|local|shell oracle64-10.0.2
```

Remove a JDK version:

```console
$ jenv remove oracle64-10.0.2
```
