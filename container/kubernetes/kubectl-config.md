# `kubectl` Config

After installed `kubectl`, create configuration files for different environments in `~/.kube`. The schema looks something like:

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

  - name: <username>
    user:
      token: ...
```

Set env variables in `~/.bashrc`, for example:

```
export KUBECONFIG=~/.kube/kubeconfig-context:~/.kube/kubeconfig-staging:~/.kube/kubeconfig-production
source <(kubectl completion bash)
```

The `kubeconfig-context` file only selects the current active context, i.e. the (cluster, user, namespace) combination. We can check it with

```console
$ kubectl config get-contexts
```

A default namespace can also be set through the console:

```console
$ kubectl config set-context <context-name> --namespace <namespace>
$ kubectl config use-context <context-name>
```
