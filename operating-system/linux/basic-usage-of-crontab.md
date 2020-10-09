# Basic Usage of Crontab

In Ubuntu, the system cron file is `/etc/crontab`, format is:

```
# m h dom mon dow  command
  * *  *   *   *  <command>
```
For example, executing a script at 10:00 every weekday:

```
0 10 * * 1-5 /home/yuka/some-script.sh
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
# service cron start
# service cron stop
# service cron restart
```

To remove all cron jobs:

```console
$ crontab -r
```

Use `sudo` to do the same operations for the root crontab.

## Logs

System logs:

```console
$ grep CRON /var/log/syslog
```

Add the following after the command to redirect output (`stdout` and `stderror`) to a file:

```
<command> > /path/to/cronjob.log 2>&1
```
