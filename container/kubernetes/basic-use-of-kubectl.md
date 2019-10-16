# Basic Use of `kubectl`

**List all the pods for a project**:

```
kubectl -n <namespace> get pod [-l <label-key>=<label-value>]
```

The `label-key` could be something like `project`, `app` as defined in the metadata for a project.

Add `-w` (wait) to follow the creation and termination status of the pods.

**Show details of a pod**:

```
kubectl -n <namespace> describe pod <pod-name>
```

**Delete a pod**:

```
kubectl -n <namespace> delete pod <pod-name>
```

**Delete a pod forcefully without confirmation that the running pod has been terminated**:

```
kubectl -n <namespace> delete pod <pod-name> --grace-period=0 --force
```

**Execute command in a container in a pod**:

```
kubectl -n <namespace> exec <pod-name> -c <container-name> <command>
```

`command` could be like `env` etc.

Add `-it` and use `bash` to enter the container and run an interactive bash.

**Show logs of a container**:

```
kubectl -n <namespace> logs -f <pod-name> <container-name>
```

**Output configmaps of a pod in `yaml` format**:

```
kubectl -n <namespace> get cm|configmaps <pod-name> -o yaml
```

**Restart a deployment/pods**:

Since v1.15.0:
```
kubectl -n <namespace> rollout restart deployment <deployment-name>
```
