# Check Listening Ports

Make sure `netstat` is installed.

The following command can be used to list all the TCP port connections:

```console
$ netstat -ant
```
If we only want to check all the TCP ports which the server is listening to, we can grep the state like:

```console
$ netstat -ant | grep "LISTEN"
```

or just run:

```console
$ netstat -lt
```

Check a specific port:

``` console
$ netstat -lt | grep <port>
```

For UDP ports just change the socket option `-t` or `--tcp` to `-u` or `--udp`.
