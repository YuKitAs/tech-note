# Use of Init Containers

[Init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) can be used to execute setup scripts before the app container in a pod, if the scripts are not present in the app image.

For example, if the app container has a read-only root filesystem and runs as a non-root user, but we need to write to a custom directory, we can use an init container to mount a volume and grant permissions as root user to a specific user like 1000 which will be used to write to the directory.

```yaml
spec:
    spec:
      initContainers:
        - name: grant-permissions
          image: busybox
          command: [ "sh", "-c", "chown -R 1000:1000 /path-to-write" ]
          volumeMounts:
            - name: some-volume
              mountPath: /path-to-write
          securityContext:
            runAsUser: 0
```

The app container and the volume:

```yaml
spec:
    spec:
      containers:
        - name: app
          image: some-image
          volumeMounts:
            - name: some-volume
              mountPath: /path-to-write
          securityContext:
            runAsNonRoot: true
            runAsUser: 1000
            runAsGroup: 1000
            readOnlyRootFilesystem: true
      volumes:
        - name: some-volume
          emptyDir: {}
```
