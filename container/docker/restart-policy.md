# Restart Policy

The restart policy can be specified with `docker run`:

```console
$ docker run --restart=always
```

So the container will be automatically restarted on daemon startup, regardless of the current state of the container. The default policy is `no`.

Check restart policy:

```console
$ docker inspect <container> | grep -A3 RestartPolicy
"RestartPolicy": {
    "Name": "always",
    "MaximumRetryCount": 0
},
```

Update restart policy for a container:

```console
$ docker update --restart=no <container>
```
