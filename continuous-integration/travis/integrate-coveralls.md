# Integrate Coveralls

The following steps are used to integrate [coveralls-gradle-plugin](https://github.com/kt3k/coveralls-gradle-plugin) with [JaCoCo plugin](https://docs.gradle.org/current/userguide/jacoco_plugin.html) for my Gradle project:

1. Add the plugins into `build.gradle`:

  ```gradle
  plugins {
      id 'jacoco'
      id 'com.github.kt3k.coveralls' version '2.6.3'
  }

  jacocoTestReport {
      reports {
          xml.enabled = true
          html.enabled = true
      }
  }
  ```

2. In `.travis.yml`, after running the script(s) for test:

  ```yaml
  after_success:
    - ./gradlew jacocoTestReport coveralls
  ```

3. Login to [Coveralls](https://coveralls.io/) and add the repo. For public open-source repos I don't need to use the `repo_token` or to create the `.coveralls.yml` file at all.

4. After Travis running the build successfully, the test coverage will be shown in Coveralls. Then I can choose to add the badge to my `README.md`.
