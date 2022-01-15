# Job Template Inheritance

[YAML anchors](https://docs.gitlab.com/ee/ci/yaml/#anchors) were introduced in GitLab 8.6 to inherit shared properties (image, services, script etc.) from a job template, like:

```yaml
.job_template: &job_definition
  image: ruby:2.1
  services:
    - postgres
    - redis

job1:
  <<: *job_definition
  script:
    - script1

job2:
  <<: *job_definition
  script:
    - script2
```

Since GitLab 11.3 [`extends`](https://docs.gitlab.com/ee/ci/yaml/#extends) is introduced to replace the YAML anchors:

```yaml
.job_template:
  image: ruby:2.1
  services:
    - postgres
    - redis

job1:
  extends: .job_template
  script:
    - script1

job2:
  extends: .job_template
  script:
    - script2
```

Advantages of `extends` include better readability and multi-level inheritance support.
