# Check IP Address

## Network interface and IP address

On Linux, the `ip` command is used to show all the network interfaces either enabled or disabled, while `/sbin/ifconfig` only shows enabled interfaces. So we can use the following command to check all the interfaces together with IP addresses:

```console
$ ip addr show
```

## IP address for the host

The following commands can be used to check the IP address of `localhost`:

```console
$ host localhost
$ hostname -i
```

To list all IP addresses for the host:

```console
$ hostname -I
```

## Public IP address

The public IP address can be found "everywhere", for example search "ip" on Google or simply use `curl ifconfig.me` to print it on the console.
