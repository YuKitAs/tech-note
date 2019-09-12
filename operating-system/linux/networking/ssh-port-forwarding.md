# SSH Port Forwarding

## Local forwarding

Use the `-L` option to forward a port from the local client machine to the server machine:

```console
$ ssh -L 8080:localhost:80 server.example.com
```

As the connection to host `server.example.com` will be opened, any connection to `localhost:80` will be forwarded to `server.example.com:8080`.

## Remote forwarding

Use the `-R` option to forward a port from the remote server to the client machine.
