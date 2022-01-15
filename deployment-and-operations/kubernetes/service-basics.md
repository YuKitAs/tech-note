# Service Basics

Applications running in a Kubernetes cluster find and communicate with each other and the outside world, through the Service abstraction. There are different types of Service like `ClusterIp`, `NodePort` and `LoadBalancer`.

A Service can be created with `kubectl expose` based on a Deployment:

```console
$ kubectl expose deployment/<deployment-name> \
  --name=<service-name> \
  --port=<service-port> \
  --target-port=<target-port>
  --type=<service-type>
```

`port` is the abstracted Service port which can be used by other Pods to access the service. `targetPort` is the port the container accepts traffic on, by default it's the same value as the `port`, it can also be a String referring to the name of a port in the backend Pods. Service maps an incoming port to any `targetPort`.

A Service YAML manifest may look like:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ...
  annotations:
    ...
  labels:
    ...
spec:
  type: NodePort
  ports:
    - name: http
      port: 80
      targetPort: nginx
  selector:
    ...
```

## References

* [Connecting Applications with Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/), Kubernetes Concepts
* [Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/), Kubernetes Tutorials
