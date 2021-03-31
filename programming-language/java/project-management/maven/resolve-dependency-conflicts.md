# Resolve Dependency Conflicts

Resolve dependency version conflicts (with a nearest-win strategy) and display conflicting dependencies that were omitted:

```console
mvn dependency:tree -Dverbose -Dincludes=<dependency>
```

where the pattern of `<dependency>` is as follows (each segment is optional):

```
[groupId]:[artifactId]:[type]:[version]
```
