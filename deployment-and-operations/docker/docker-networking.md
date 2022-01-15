# Docker Networking

Default Docker network drivers

* `bridge`: usually used when applications run in standalone containers that need to communicate

* `host`: use the host's networking directly

* `none`: disable all networking, usually used with a custom network driver

**List networks**:

```console
$ docker network ls
```

**Inspect detailed information of a network**:

```console
$ docker network inspect <network_name>
```

**Remove a network**:

```console
$ docker network rm <network_name>
```

**Remove all unused networks**:

```console
$ docker network prune
```

**Create a user-defined network**:

```console
$ docker network create <network_name>
```

Containers that use the same network (specified by `--network <network_name>`) can communicate with other with the container name as host name.

## Reference

* [Networking Overview](https://docs.docker.com/network/), Docker Documentation
