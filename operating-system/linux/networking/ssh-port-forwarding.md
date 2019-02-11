# SSH Port Forwarding

For local forwarding, use the `-L` option like:

```console
$ ssh -L 8080:localhost:8080 server.example.com
```

As the connection to host `server.example.com` will be opened, any connection to `localhost:8080` will be forwarded to `server.example.com:8080`.
