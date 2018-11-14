# Get Container IP Address

Use the following command to output the IP address of a Docker container (`-f` is short for --format``):

```console
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-ID|container-name>
```
