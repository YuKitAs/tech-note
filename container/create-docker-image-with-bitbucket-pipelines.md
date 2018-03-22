# Create Docker Image with Bitbucket Pipelines

[Bitbucket Pipelines](https://confluence.atlassian.com/bitbucket/get-started-with-bitbucket-pipelines-792298921.html) allows automated builds, tests and deployment based on a configuration file in a Bitbucket repository.

For example, we have a Gradle project with Gradle Wrapper installed, we can simply write the `bitbucket-pipelines.yml` like this:

```yaml
pipelines:
  default:
    - step:
        name: Gradle build
        image: java:8
        script:
          - bash ./gradlew clean build
```

In this example, after `gradlew build`, a new `build` directory is produced, if we want to copy the files in `build` to a Docker image, we need to configure these files as artifacts to make them accessible in the next step. Add the following configuration to step `Gradle build`:


```yaml
artifactes:
  - build/**
```

Then we need a `Dockerfile` for creating a Docker image. The content could be something like:

```Dockerfile
FROM debian:stable
ADD build/libs/test-app.jar test-app.jar
CMD ["java", "-jar", "test-app.jar"]
```

Then we can use Bitbucket pipelines to run Docker commands by adding Docker as a service (officially recommended). The whole configuration file will be like this:

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
    - step:
        name: Docker create image
        trigger: manual
        script:
          - docker build -t test-app .
        services:
          - docker
```

If not set `trigger: manual`, the step will run automatically and cost bitbucket build minutes, which is unnecessary. But the first step cannot be manual.

To push the image to a Docker registry we need to add `docker login` and `docker push` commands before and after `docker build` with information for the registry.
