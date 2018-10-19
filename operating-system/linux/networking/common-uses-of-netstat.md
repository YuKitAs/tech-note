# Common Uses of `netstat`

## List port connections

The following command can be used to list all the TCP port connections (for UDP ports just use the socket option `-u` or `--udp`, the same below):

```console
$ netstat -ant
```

## List listening ports

If we only want to check all the TCP ports which the server is listening to, we can grep the state like:

```console
$ netstat -ant | grep "LISTEN"
```

or just run:

```console
$ netstat -lt
```

## Check a specific port

To check the process(es) listening to a specific port:

```console
$ netstat -tulpn | grep <port>
```

* To kill all the processes associated with the port: `# fuser -k 8000/tcp`
