# Ingress Basics

An Ingress is an API object in the Kubernetes (since v1.1) that exposes HTTP and HTTPS routes outside the cluster to services within the cluster, it requires an Ingress Controller (e.g. Nginx, Traefik) to be deployed in the cluster. Traffic routing is controlled by `rules` defined in Ingress spec, like:

```yaml
apiVersion: extensions/v1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: ...
    http:
      paths:
      - path: /foo
        backend:
          serviceName: ...
          servicePort: 80
```

HTTP and HTTPS requests to the Ingress matching the `host` and `path` of the rule will be sent to the `backend` defined with `serviceName` and `servicePort`. The `host` is optional, when not specified, then the rule will be applied to all inbound HTTP traffic through the IP address. If the requests don't match any `host` or `path`, the traffic will be routed to a default `backend`, which is also used when Ingress has no `rules`.

An Ingress can be secured with a secret that contains a [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) private key and certificate.
