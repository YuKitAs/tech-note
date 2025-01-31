# Basic Use of IBM Cloud Code Engine

Use IBM Cloud Code Engine to deploy and manage containerized applications.

* **Select a project**:

  ```console
  $ ibmcloud ce project select -n <project>
  ```

* **Build and run an app in the current project**:

  ```console
  $ ibmcloud ce app create --name <app-name> --image <container-image> [--registry-secret <secret-for-private-registry> --port <port> --build-context-dir <directory-containing-dockerfile> --build-source .]
  ```

  A public deployment URL (`*.cloud`) will be generated at the end which can be used to access the app.

* **List all apps**:

  ```console
  $ ibmcloud ce app list
  ```

* **Get the details of an app**:

  ```console
  $ ibmcloud ce app get -n <app-name>
  ```

* **Scale an app**:

  ```console
  $ ibmcloud ce app update --name <app-name> --min <min-instances> --max <max-instances>
  ```

* **Update a running app**:

  ```console
  $ ibmcloud ce app update --name <app-name> --image <container-image> [--registry-secret <secret-for-private-registry> --port <port> --build-context-dir <directory-containing-dockerfile> --build-source .]
  ```

* **Delete an app**:

  ```console
  $ ibmcloud ce app delete --name <app-name>
  ```
