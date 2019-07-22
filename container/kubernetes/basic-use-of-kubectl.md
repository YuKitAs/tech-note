# Basic Use of `kubectl`

**List all the pods for a project**:

```
kubectl -n <namespace> get pod -l <label-key>=<label-value> -w
```

The `label-key` could be something like `project`, `app` as defined in the metadata for a project.

`-w` means wait, so that we can follow the creation and termination of the pods.

**Show details of a pod**:

```
kubectl -n <namespace> describe pod <pod-name>
```

**Enter an container in a pod**:

```
kubectl -n <namespace> exec <pod-name> -it -c <container-name> bash
```

Instead of `bash`, other commands can also be executed directly, e.g. `sh/env`.

**Show logs of an application**:

```
kubectl -n <namespace> logs -f pod/<pod-name> <application-container-name>
```

**Output configmaps of a pod in `yaml` format**:

```
kubectl -n <namespace> get configmaps <pod-name> -o yaml
```

**Restart a deployment/pods**:

Since v1.15.0:
```
kubectl -n <namespace> rollout restart deployment <deployment-name>
```
