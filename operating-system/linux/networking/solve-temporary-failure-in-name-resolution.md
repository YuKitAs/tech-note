# Solve "Temporary failure in name resolution"

A temporary fix for the following SSH connection error:

```
ssh: Could not resolve hostname <hostname>: Temporary failure in name resolution
```

In `/etc/resolv.conf`, change `nameserver` to `8.8.8.8`.
