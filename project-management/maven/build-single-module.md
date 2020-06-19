# Build Single Module

In multi-module projects, use `advanced reactor options` in the parent directory to build a specific module:

```console
$ mvn install -pl <artifactId> -am
```
