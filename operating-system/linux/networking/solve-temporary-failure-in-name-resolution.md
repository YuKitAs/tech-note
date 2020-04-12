# Solve "Temporary failure in name resolution"

**Approach 1**

A temporary fix for the following SSH connection error:

```
ssh: Could not resolve hostname <hostname>: Temporary failure in name resolution
```

In `/etc/resolv.conf`, change `nameserver` to `8.8.8.8`.


**Approach 2**

In `/etc/network/interfaces`, add:

```
dns-nameservers 8.8.8.8 8.8.4.4
```

Restart `network-manager`:

```console
$ sudo systemctl restart network-manager
```
