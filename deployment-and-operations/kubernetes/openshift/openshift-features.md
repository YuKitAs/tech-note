# OpenShift Features

OpenShift CLI (`oc`) extends `kubectl` by adding the following key OpenShift-specific features:

## Project Management

`oc project` can be used to switch between projects (namespaces) directly and replace `kubectl config set-context`.

## Routing

An OpenShift Route is a way to expose a service running inside an OpenShift cluster to the outside world, it can be created automatically with

```console
$ oc expose svc <service-name> --hostname=<service.com>
```

or manually like

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: my-app-route
spec:
  host: my-app.example.com
  to:
    kind: Service
    name: my-app
  tls:
    termination: edge  # HTTPS termination at the router
```

While in Kubernetes an Ingress Controller needs to be manually installed.

## Image Build & Management

OpenShift can build an app directly from source code (S2I) with pre-built builder images like

```console
$ oc new-app python~https://github.com/example/repo.git
```

While in Kubernete the image needs to be built manually with Dockerfiles, slower but fully customizable.

OpenShift has its internal registry and can import images from external registries with `oc import-image`, while `kubectl` can only pull images from external registries and doesn't have internal image management.

## User Management & RBAC

OpenShift has built-in authentication (Oauth, LDAP, etc.) and simplifies RBAC with `oc policy` or `oc adm policy` (cluster-wide), while Kubernetes needs service accounts and external identity providers for user management.

## Deployment Configs

OpenShift has `DeploymentConfigs` (`dc`) which uses triggers for auto-redeploy on config or image changes and allows more flexible rolling updates and rollback strategies.
