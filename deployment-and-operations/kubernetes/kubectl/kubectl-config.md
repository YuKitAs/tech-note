# `kubectl` Config

`kubectl` configuration files should be located in `~/.kube/`. The default config is `~/.kube/config`. The schema looks like:

```
kind: Config
apiVersion: v1

contexts:
  - name: <context-name>
    context:
      cluster: <context-cluster>
      user: <context-user>
      namespace: <context-namespace>

clusters:
  - name: <cluster-name>
    cluster:
      server: <cluster-server>
      certificate-authority-data: ...

users:
  - name: <user-name>
    user:
      certificate-authority-data: ...
```

Set environment variable `KUBECONFIG` in `~/.bashrc` with actual config file paths. For example:

```
export KUBECONFIG=~/.kube/config-staging:~/.kube/config-production
```

Check config:

```console
$ kubectl config view
```

A context associated with a default namespace can be created with:

```console
$ kubectl config set-context <context-name> --current --namespace <namespace>
```

List all contexts:

```console
$ kubectl config get-contexts
```

Check current context:

```console
$ kubectl config current-context
```

Use another context as default:

```console
$ kubectl config use-context <context-name>
```
