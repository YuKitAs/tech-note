# Use Artifacts in Steps

When we need to use files generated in a former step, we must configure these files as artifacts.

Take a Gradle project for instance, if we want to access the `build` directory after the build step, we should write the `bitbucket-pipelines.yml` like this:

```yaml
pipelines:
  default:
    - step:
        name: Gradle build
        image: java:8
        script:
          - bash ./gradlew clean build
        artifacts:
          - build/**
```

Only in this way can the files in `build` be copied and shared with the later depolyment step.
