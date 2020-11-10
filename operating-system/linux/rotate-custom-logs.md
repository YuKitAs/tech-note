# Rotate Custom Logs

Create a configuration file `/etc/logrotate.d/example.conf` with the log file path and options like:

```
/path/to/custom.log {
  weekly
  rotate 7
  maxsize 50M
  missingok
  compress
}
```

For explanation and more options see `man logrotate`.

Dry-run for test:

```console
$ logrotate -d /etc/logrotate.d/example.conf
```

Normally, `logrotate` is run as a daily cron job. Execute immediately (forcefully):

```console
$ logrotate -f -v /etc/logrotate.d/example.conf
```
