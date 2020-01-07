# Rollout Deployments with Updated ConfigMaps and Secrets

When ConfigMaps and Secrets injected as configuration files have been changed, if the deployment spec didn't change, the application will still run with the old configurations. In order to update the deployment's annotation section automatically, we need to add the checksum of the ConfigMap or Secret into `spec.template.metadata.annotations` as follows:

```yaml
kind: Deployment
spec:
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
```
