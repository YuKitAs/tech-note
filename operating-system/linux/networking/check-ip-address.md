# Check IP Address

## Network interface and IP address

On Linux, the `ip` command is used to show all the network interfaces either enabled or disabled, while `/sbin/ifconfig` only shows enabled interfaces. So we can use the following command to check all the interfaces together with IP addresses:

```console
$ ip addr show
```

## IP address for the host

The IP address of `localhost` can be checked with `host localhost` or just `ping localhost`, usually it's `127.0.0.1`.

To list all IP addresses for the host:

```console
$ hostname -I
```

## Ethernet interface IPv4 address

This IPv4 address (usually `192.168.*.*`) will be listed by `hostname -I` mentioned above. It can also be easily found in network connection information of the computer.

## Public IP address

The public IP address can be found "everywhere". For example, search "ip" on Google or use `curl ifconfig.co` to check the IPv6 address, use `curl ifconfig.me` to get the IPv4 address and so on.
