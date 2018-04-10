# Use Gradle Wrapper

Each Gradle Wrapper is tied to a specific version of Gradle, as it will download the corresponding Gradle distribution und use it to execute the build. Using Gradle Wrapper can ensure version consistency across different machines.

In the project root, build the Gradle wrapper by running

```console
$ gradle wrapper [--gradle-version <version>]
```

Run `gradlew` to execute Gradle tasks (make sure the script is executable):

```console
./gradlew <command>
```
