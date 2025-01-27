# Task and Pipeline

## Task

* Define `Task` resource in `tasks.yaml`:

  ```yaml
  apiVersion: tekton.dev/v1beta1
  kind: Task
  metadata:
    name: echo # task name
  spec:
    params:
      - name: message
        description: The message to echo # optional
        type: string # optional
    steps:
      - name: echo # step name
        image: alpine:3
        command: [/bin/echo]
        args: ["$(params.message)"]

  ```

* Apply `Task`:

  ```console
  $ kubectl apply -f tasks.yaml
  ```

* List tasks:

  ```console
  $ kubectl get task
  ```

  or

  ```console
  $ tkn task ls
  ```

## Pipeline

* Define `Pipeline` resource in `pipeline.yaml`:

  ```yaml
  apiVersion: tekton.dev/v1beta1
  kind: Pipeline
  metadata:
    name: cd-pipeline # pipeline name
  spec:
    params:
      - name: repo-name
      - name: branch
        default: master
    tasks:
      - name: lint
        taskRef:
          name: echo
        params:
        - name: message
          value: "Linting..."
      - name: tests
        taskRef:
          name: echo
        params:
        - name: message
          value: "Running tests..."
        runAfter:
          - lint
      - name: build
        taskRef:
          name: echo
        params:
        - name: message
          value: "Building image for $(params.repo-name) ..."
        runAfter:
          - tests
      - name: deploy
        taskRef:
          name: echo
        params:
        - name: message
          value: "Deploying $(params.branch) branch of $(params.repo-name) ..."
        runAfter:
          - build
  ```

* Apply `Pipeline`:

  ```console
  $ kubectl apply -f pipeline.yaml
  ```

* List pipelines:

  ```console
  $ kubectl get pipeline
  ```

  or

  ```console
  $ tkn pipeline ls
  ```

* Run pipeline with Tekton:

  ```console
  $ tkn pipeline start --showlog cd-pipeline -p repo-name="template-service"
  ```

  Log:

  ```
  PipelineRun started: cd-pipeline-run-t2r57
  Waiting for logs to be available...
  [lint : echo] Linting...

  [tests : echo] Running tests...

  [build : echo] Building image for template-service ...

  [deploy : echo] Deploying master branch of template-service ...
  ```
