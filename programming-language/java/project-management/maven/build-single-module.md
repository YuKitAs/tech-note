# Build Single Module

In multi-module projects, use `advanced reactor options` in the parent directory to build a specific module with its required modules (`--also-make`):

```console
$ mvn package -pl <directory> -am
$ mvn package -pl :<artifactId> -am
```
