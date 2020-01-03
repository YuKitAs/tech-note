# Docker Networking

Default Docker network drivers:

* `bridge`: usually used when applications run in standalone containers that need to communicate

* `host`: use the host's networking directly

* `none`: disable all networking, usually used with a custom network driver

**List networks**:

```console
docker network ls
```

**Inspect detailed information of a network**:

```console
docker network inspect <container_id>
```

**Remove a network**:

```console
docker network rm <container_id>
```

**Remove all unused networks**:

```console
docker network prune
```

## Reference

* [Networking Overview](https://docs.docker.com/network/), Docker Documentation
