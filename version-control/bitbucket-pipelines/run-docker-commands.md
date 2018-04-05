# Run Docker Commands

We can use Bitbucket pipelines to run Docker commands by adding Docker as a service (officially recommended). The configuration file could look like this:

```yaml
pipelines:
  default:
    - step:
        name: Docker create image
        trigger: manual
        script:
          - docker version
          - docker login <registry> -u $DOCKER_USER -p $DOCKER_PASSWORD
          - docker build [-f path/to/Dockerfile] -t <image-name>[:tag] .
          - docker push <image-name>[:tag]
        services:
          - docker
```

If not set `trigger: manual`, the step will run automatically and cost bitbucket build minutes, which is unnecessary. However, if it's the first step, then it cannot be manual, we need to add `[skip ci]` in the commit message to avoid automatical running.
