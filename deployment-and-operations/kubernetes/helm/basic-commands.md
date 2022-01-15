# Basic Commands


**[Helm Template](https://helm.sh/docs/helm/helm_template/)**

Render templates locally and display the output, but won't validate the chart from the server-side (e.g. if an API is supported).

```console
$ helm template [name] [chart] [flags]
```

**[Helm Dependency Update](https://helm.sh/docs/helm/helm_dependency_update/)**

Verifies the required charts specified in `Chart.yaml` are present in `charts/` with correct versions.

```console
$ helm dependency update [chart] [flags]
```

**[Helm Package](https://helm.sh/docs/helm/helm_package/)**

Package a chart directory into a versioned chart archive.

```console
$ helm package [chart_path] [...] [flags]
```


**[Helm Repo Add](https://helm.sh/docs/helm/helm_repo_add/)**

Add a chart repository.

```console
$ helm repo add [name] [url] [flags]
```

**[Helm Install](https://helm.sh/docs/helm/helm_install/)**

Install a chart archive into k8s cluster (the cluster that `kubectl` is pointing to).

```console
$ helm install [name] [chart] [flags]
```

## Pushing Helm chart to GitLab registry

```bash
helm plugin install https://github.com/chartmuseum/helm-push
helm registry login --password-stdin -u "$CI_REGISTRY_USER" "$CI_REGISTRY" <<<"$CI_REGISTRY_PASSWORD"
helm package "${CHARTSDIR}-dist/${CHARTNAME}"
# plugin command to push chart to ChartMuseum
helm cm-push "${CHARTSDIR}-dist/${CHARTNAME}" gitlab
# list releases
helm list
```

## Fetching Helm chart from GitLab registry

```bash
helm registry login --password-stdin -u "$CI_REGISTRY_USER" "$CI_REGISTRY" <<<"$CI_REGISTRY_PASSWORD"
helm chart pull "${CI_REGISTRY}/${CHARTPATH}:${CHARTVERSION}"
helm chart export "${CI_REGISTRY}/${CHARTPATH}:${CHARTVERSION}"
```
