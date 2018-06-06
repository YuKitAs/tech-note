# Set `vm.max_map_count`

Elasticsearch uses a [`mmapfs`](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-store.html#default_fs) directory by default to store its indices. `max_map_count` of virtual machine needs to be at least 262144 for production use.

It can be set with the following command:

```console
$ sudo sysctl -w vm.max_map_count=262144
```

To set it permanently, update it in `/etc/sysctl.conf` and reboot. Use `sysctl vm.max_map_count` to verify the setting.
