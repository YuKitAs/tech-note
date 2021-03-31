# Set Version and Deploy

Set a specific version for all modules like:

```console
$ mvn versions:set -DnewVersion=1.0.0-debug
```

Then the version in `pom.xml` will be updated to `<version>1.0.0-debug</version>` and the old `pom.xml` will be automatically backed up.

Deploy artifacts with the new version:

```console
$ mvn deploy
```
