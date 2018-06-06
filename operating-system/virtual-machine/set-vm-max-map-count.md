# Set `vm.max_map_count`

To run Elasticsearch 5.0 the `max_map_count` of virtual machine needs to be at least 262144 for production use.

This setting should be in `/etc/sysctl.conf` so it can be set with the following command:

```console
$ sudo sysctl -w vm.max_map_count=262144
```
