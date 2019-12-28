# Getting Started

## Initialize the Project

1. Bootstrap a Maven project with the Quarkus Maven plugin:

  ```console
  $ mvn io.quarkus:quarkus-maven-plugin:1.1.0.Final:create \
      -DprojectGroupId=<group-id> \
      -DprojectArtifactId=<artifact-id> \
      -DprojectVersion=<version> \
      -DclassName="com.yukitas.MainResource"
  ```

  By adding `-DbuildTool=gradle` we can setup a Gradle project instead.

2. Another way to bootstrap the project with extensions is to generate it from https://code.quarkus.io/.

## Run the Application

  There is no need to have an `Application` class. The application is accessible on `http://localhost:8080` by default.

1. We can use `./mvnw compile quarkus:dev` to run this application in development mode, where the changes will automatically take effect so that we don't have to re-run the application.

2. Or after packaging the application, run the generated executable with:

  ```console
  $ java -jar target/<artifact-id>-<version>-runner.jar
  ```
