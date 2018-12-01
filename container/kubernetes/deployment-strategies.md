# Deployment Strategies

A Kubernetes Deployment instruct the Kubernetes master how to create and update application instances onto individual Nodes in the cluster. To achieve a self-healing system, it supports the following two rollout strategies:

**1. Recreate Strategy**

Simply updates the ReplicaSet it manages to use the new image and terminates all of the Pods associated with the Deployment. Though it's fast and simple, obviously it will result in some downtime, so it should only be used for test depolyments.


**2. RollingUpdate Strategy**

Preferable for any user-facing service but slower than `Recreate`. Updates a few Pods at a time, moving incrementally until all of the Pods are running the new version of the service. It can be configured with `maxUnavailable` (how many Pods can be unavailable during the update) and `maxSurge` (how many Pods can be added at a time) parameters.

As ReplicaSets manage Pods, the top-level Deployment object manages ReplicaSets. A Deployment manifest may look like this:

```yaml
appVersion: v1
kind: Deployment
metadata:
  name: ...
  labels:
    ...
  annotations:
    ...
spec:
  replicas: 2
  selector:
    matchLabels:
      ...
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      annotations:
        ...
      labels:
        ...
    spec:
      containers:
        - name: ...
          image: ...
          imagePullPolicy: Always
          ...
```
