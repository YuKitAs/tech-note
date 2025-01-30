# Workspace and PVC

Workspace is the abstraction that Tekton uses to define shared storage for tasks and pipelines. Workspace can be declared in tasks or pipelines like:

```yaml
spec:
  workspaces:
    - name: shared-data # Workspace required by the pipeline
  tasks:
    - name: my-task
      taskRef:
        name: example-task
      workspaces:
        - name: example-task-workspace # Workspace required by example-task
          workspace: shared-data # Map the pipeline's workspace to the workspace of example-task
```

A PVC (PersistentVolumeClaim) is a request for storage in Kubernetes. It allows a Tekton pipeline or task to persist data by claiming storage from a Kubernetes cluster's storage resources (Persistent Volumes). The PVC definition looks like this:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMount: FileSystem
  resources:
    requests:
      storage: 1Gi
```

In a PipelineRun definition, the actual storage configuration is provided to the workspace like:

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: pipeline-run-
spec:
  pipelineRef:
    name: my-pipeline
  workspaces:
    - name: shared-data
      persistentVolumeClaim:
        claimName: my-pvc # Bind to a specific PVC
```
