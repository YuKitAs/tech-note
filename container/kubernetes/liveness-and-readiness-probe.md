# Liveness and Readiness Probe

In Kubernetes, _process health checks_ are used to check whether the main process of the application is running. But as this check is not sufficient, Kubernetes also provides _liveness health checks_ to determine whether the application is running properly. Liveness probes can be defined in the Pod manifest (per container) like:

```yaml
containers:
    - image: ...
      name: ...
      livenessProbe:
        httpGet:
          path: /health
          port: 9000
        initialDelaySeconds: ...
        timeoutSeconds: ...
        periodSeconds: ..
        failureThreshold: ...
```

Containers that fail liveness checks will be restarted.

Besides, there are _readiness checks_ which check whether a container is ready to serve user requests and readiness probes are configured similarly to liveness probes. Containers that fail readiness checks will be removed from service load balancers.
