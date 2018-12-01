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

  ```yaml
  spec:
    containers:
      - name: ...
        volumeMounts:
          - name: <config-volume-name>
          mountPath: ...
    volumes:
      - name: <config-volume-name>
        configMap:
          name: <configmap-name>
  ```

2. Environment variables: dynamically set the value of an environment variable.

  ```yaml
  spec:
    containers:
      - name: ...
        env:
          - name: <ENV_VAR_1>
            valueFrom:
              configMapKeyRef:
                name: <configmap-name>
                key: <param-key>
          - name: <ENV_VAR_2>
            valueFrom:
              secretKeyRef:
                ...
  ```

3. Command-line arguments: dynamically create command-line arguments build on enviroenment variables.

  ```yaml
  spec:
    containers:
      - name: ...
        command: [ "/bin/sh", "-c", "echo ${ENV_VAR_1}" ]
  ```
