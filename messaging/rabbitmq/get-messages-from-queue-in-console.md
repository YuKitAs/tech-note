# Get Messages from Queue in Console

If using the console, just run the following command with `rabbitmqadmin` to get messages from a queue, but pay attention, this is a destructive action:

```console
$ rabbitmqadmin get queue=<queue-name>
```
