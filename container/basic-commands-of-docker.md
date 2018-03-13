# Basic Commands of Docker

List all Docker commands:

```console
$ docker
```

Show Docker version and info:

```console
$ docker --version
$ docker info
```

Show Docker status:

```console
$ sudo service docker status
```

List all Docker images:

```console
$ docker image ls
```

Execute a Docker image:

```console
$ docker run <image-ID|image-name>
```

Remove a Docker image:

```console
$ docker rmi <image-ID>
```

Remove all Docker images:

```console
$ docker rmi $(docker images -q)
```

`-q` means only displaying IDs.

List running Docker containers:

```console
$ docker container ls
```

or

```console
$ docker ps
```

List all Docker containers:

```console
$ docker container ls --all
```

or

```console
$ docker ps -a
```

Remove a Docker container:

```console
$ docker rm <container-ID>
```

Remove all Docker containers:

```console
$ docker rm $(docker ps -aq)
```
