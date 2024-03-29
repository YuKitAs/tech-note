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

## Pod

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

## Deployment and Service

**Expose a deployment as a new service**:

Creates a ClusterIP Service with an IP address that's accessible within the cluster.

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

**Get a deployment**:

```
kubectl get deploy|deployment
```

Add `-o wide` to get deployments with additional info like containers and images.

**Create a tunnel between a localhost and a pod**:

```
kubectl port-forward deployment/<deployment-name> <local-port>:<pod-port>
```
```
kubectl port-forward <pod-name> <local-port>:<pod-port>
```

**Update container image for a deployment**:

```
kubectl set image deploy|deployment <deployment-name> <container-name>=<new-image-name>:<new-tag>
```

**Restart a deployment**:

```
kubectl rollout restart deploy|deployment <deployment-name>
```

**Rollback a deployment**:

Rollback to a previous stable state of the deployment.

```
kubectl rollout undo deploy|deployment <deployment-name>
```

**Get rollout status**:

```
kubectl rollout status deploy|deployment <deployment-name>
```

**Autoscale deployment (HPA)**:

Creates an HPA resource associated with the specified deployment.

```
kubectl autoscale deployment <deployment-name> --min=<min-replicas> --max=<max-replicas> --cpu-percent=<cpu-utilization-target>
```

**Check HPA status**:

```
kubectl get hpa <hpa-name> --watch
```

## Setup

**Completion for alias**:

If an alias is set for `kubectl`, add the following config to `~/.bashrc` to use the default completion:

```
complete -o default -F __start_kubectl <kubectl_alias>
```
