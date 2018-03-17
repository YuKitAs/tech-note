# Maven Build Lifecycle

The default `jar` packaging will bind the following goals to build phases of the default lifecycle:

* **process-resources**: copy and process the resources into the destination directory, ready for packaging.

* **compile**: compile the source code of the project.

* **process-test-resources**: copy and process the resources into the test destination directory.

* **test-compile**: compile the test source code into the test destination directory.

* **test**: test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed.

* **package**: take the compiled code and package it in its distributable format, e.g. a JAR.

* **install**: install the package into the local repository, for use as a dependency in other projects locally.

* **deploy**: done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects.

## Reference

* [Introduction to the Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html), Apache Maven Project.
