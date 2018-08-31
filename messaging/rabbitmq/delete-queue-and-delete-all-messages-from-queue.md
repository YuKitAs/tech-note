# Delete Queue and Delete all Messages from Queue

Delete a single queue with `rabbitmqadmin`:

```console
$ rabbitmqadmin delete queue name=<queue_name>
```

Delete all messages from a single queue with `rabbitmqctl`:

```console
# rabbitmqctl purge_queue <queue_name>
```
