# Event Triggers

External events can fire a trigger that starts a pipeline. We need an `EventListener` (Pod) to listen to the events, a `TriggerBinding` that forwards the parameters from the events to the `TriggerTemplate` for the pipeline to run (`PipelineRun`). Below is an example to define a flow.

`EventListener`:

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: cd-listener # EventListener name
spec:
  serviceAccountName: pipeline-sa
  triggers:
    - bindings:
      - ref: cd-binding # TriggerBinding name
      template:
        ref: cd-template # TriggerTemplate name
```

`TriggerBinding`:

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerBinding
metadata:
  name: cd-binding
spec:
  params:
    - name: repository
      value: $(body.repository.url) # parameter from event
```

`TriggerTemplate` with `PipelineRun`:

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerTemplate
metadata:
  name: cd-template
spec:
  params:
    - name: repository
  resourcetemplates:
    - apiVersion: tekton.dev/v1beta1
      kind: PipelineRun
      metadata:
        generateName: cd-pipeline-run- # prefix for PipelineRun name
      spec:
        serviceAccountName: pipeline-sa
        pipelineRef:
          name: cd-pipeline
        params:
          - name: repo-url
            value: $(tt.params.repository) # parameter of the TriggerTemplate
```
