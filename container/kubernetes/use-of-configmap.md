# Use of ConfigMap

A ConfigMap in Kubernetes can be regarded as a set of key/value pairs used when defining the environment or command-line for the containers. It can be created with a config file on disk:

```console
$ kubectl create configmap <configmap-name> \
--from-file=<config-file> \
--from-literal=<param-key>=<param-value>
```

The equivalent YAML (`kubectl get configmaps <configmap-name> -o yaml`) is:

```yaml
apiVersion: v1
data:
  <param-key>: <param-value>
  <config-file>: |
    # Content of the config-file
kind: ConfigMap
metadata:
  name: <configmap-name>
  ...
```

There are three ways to use a ConfigMap:

1. Filesystem: create a new volume inside the Pod and point at the ConfigMap to mount.
2. Environment variables
3. Command-line arguments
