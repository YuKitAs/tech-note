# Labels and Annotations

Labels are annotations are both key/value pairs to store metadata for Kubernetes objects.

Normally, labels are used to identify and group objects (like `name`, `env`), and Kubernetes objects can be filtered based on labels with label selectors. Annotation are used to provide extra information for communication between external systems, and thus the annotation keys are usually prefixed with a namespace like `kubernetes.io/`.

Though it's a matter of taste when to use label or annotation, it's suggested that we add information to an object as annotation and promote it to a label if a selector is needed.
