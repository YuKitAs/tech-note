# Define Volumes

In the Pod manifest, define all the volumes that can be accessed by containers in a `spec.volumes` section, and in the container definition, define the volumes that are mounted into a particular container, like:

 like:

```yaml
metadata:
  name: foo
spec:
  volumes:
    - name: "vol-1"
      hostPath:
        path: "/var/lib/vol-1"
    - name: "vol-2"
      hostPath: ...
  containers:
    - images: ...
      name: ...
      volumeMounts:
        - mountPath: "/data"
          name: "vol-1"
        - mountPath: ...
      ...
```

Different containers can mount the same volume at different mount paths.
