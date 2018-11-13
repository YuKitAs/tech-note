# Disable Service Autostart

List all the services with:

```console
$ service --status-all
```

`[ + ]` indicates running services and `[ - ]` indicates stopped services.

Stop a service from auto starting on boot up:

```console
# systemctl disable <service>
```
