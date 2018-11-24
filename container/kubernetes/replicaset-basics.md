# ReplicaSet Basics

ReplicaSets create and manage Pods but don't own the Pods they create. They use label queries to identify the set of Pods that they should manage. ReplicaSets are designed for stateless or nearly stateless services. The Pods created by ReplicaSet controller are identical and interchangeable.

The ReplicaSet controller creates and submits a Pod manifest to the API server based on the Pod template. An example of a ReplicaSet definition:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: ...
  labels:
    app: helloworld
    ver: v1
spec:
  replicas: 2
  selector:
    matchLabels:
      app: helloworld
    matchExpressions:
      - {key: ver, operator: In, values: [1, 2]}
  template:
    metadata:
      labels:
        app: ...
        version: ...
    spec:
      containers:
        - name: helloworld
          image: ...
          ports:
            - containerPort: 80
```

**Inspect a ReplicaSet**:

```console
$ kubectl describe rs <rs-name>
```

**Find a ReplicaSet from a Pod**:

```console
$ kubectl get pods <pod-name> -o yaml
```

**Find a set of Pods for a ReplicaSet**:

```console
$ kubectl get pods -l app=helloworld,version=1
```

## Reference

* Kubernetes Up & Runnung, Kelsey Hightower, Brendan Burns & Joe Beda, 2017.
