# Basic Usage of Crontab

In Ubuntu, the system cron file is `/etc/crontab`, the format is like:
```
# m h dom mon dow user  command
  * *  *   *   *  root  /home/yuka/some-script.sh
```

To edit the crontab file to add/remove a cron job:

```console
$ crontab -e
```

To list all the cron jobs:

```console
$ crontab -l
```

To start/stop/restart cron jobs:

```console
$ service cron start
$ service cron stop
$ service cron restart
```

To remove all cron jobs:

```console
$ crontab -r
```

Use `sudo` to do the same operations for the root crontab.
