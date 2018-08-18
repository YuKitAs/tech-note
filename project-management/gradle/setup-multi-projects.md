# Setup Multi-Projects

In the root project, use `gradle init` to create the following files:

```
build.gradle
gradle
gradlew
gradlew.bat
settings.gradle
```

The `settings.gradle` should already contains `rootProject.name = <project-name>`. We just need to add the names of subprojects like:

```gradle
rootProject.name = '<project-name>'
include '<subproject-1>', '<subproject-2>', ...
```

In the `build.gradle`, we can configure some properties that will be shared by all the subprojects like:

```gradle
allprojects {
    apply plugin: 'java'

    repositories {
        mavenCentral()
    }

    sourceCompatibility = 10
    targetCompatibility = 10
}
```

And for every subproject, specify individual `build.gradle`. Then we can run `./gradlew build` in the root project to build all the subprojects.
