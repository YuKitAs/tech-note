# Maven Local Repository

On Linux, all the Maven projects' dependencies will be stored in the Maven local repository. By default it's `~/.m2/repository`, the path can be specified in `~/.m2/settings.xml` like:

```xml
<settings>
  ...
  <localRepository>path/to/local/repo<localRepository>
  ...
</settings>
```

`mvn clean install` can be used to package the project and copy it to the local repository.
