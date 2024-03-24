# Basic Use of `kubectl`

**Check client and server versions**:

```
kubectl version
```

**List all Kubernetes resources**:

List all resource types along with their shortcuts, API version, and whether they are namespaced or not.

```
kubectl api-resources
```

To specify a namespace for the following commands, add `-n <namespace>`.

**Create and run an image in a pod**:

```
kubectl run <pod-name> --image=<image-name> [options]
```

**List all the pods filtered by labels**:

```
kubectl get po|pod -l <label-key>=<label-value>
```

Add `-w|--watch` to follow the creation and termination status of the pods.

Add `-o wide` to get pods with additional info like IP and node.

**Show details and status of a pod**:

```
kubectl describe po|pod <pod-name>
```

**Delete a pod**:

```
kubectl delete po|pod <pod-name>
```

**Delete a pod forcefully without confirmation that the running pod has been terminated**:

```
kubectl delete po|pod <pod-name> --grace-period=0 --force
```

**Execute command in a container in a pod**:

```
kubectl exec <pod-name> -c <container-name> <command>
```

Add `-it` and use `bash` to enter the container and run an interactive bash.

**Follow logs of a container in a pod**:

```
kubectl logs -f <pod-name> <container-name>
```

**Output configmaps of a pod in `yaml` format**:

```
kubectl get cm|configmaps <pod-name> -o yaml
```

**Expose a deployment as a new service**:

Create a ClusterIP Service with an IP address that's accessible within the cluster.

```
kubectl expose deploy|deployment <deployment-name>
```

**Get all services**:

```
kubectl get svc|service
```

**Create a proxy server between a localhost and the Kubernetes API server**:

```
kubectl proxy --port=<port>
```

The default port is 8001. The service can be accessed externally via `http://localhost:8001/api/v1/namespaces/<namespace>/services/<service-name>/proxy/`. 

**Restart a deployment**:

Since v1.15.0:
```
kubectl rollout restart deploy|deployment <deployment-name>
```

**Completion for alias**:

If an alias is set for `kubectl`, add the following config to `~/.bashrc` to use Bash completion:

```
complete -o default -F __start_kubectl <kubectl_alias>
```
