# `bootRun` with Spring Profiles

When executing `bootRun`, if we have specified different Spring profiles in `application.yml`, we can set the active profile using environment variables like:

```console
$ SPRING_PROFILES_ACTIVE=test ./gradlew clean bootRun
```
