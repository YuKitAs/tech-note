# Ubuntu Nautilus Toubleshooting

Nautilus is the file manager for GNOME on Ubuntu, used to open a directory in Terminal.

The first time I was trying to use

```console
$ nautilus .
```

I got the following error message:

```
Nautilus-Share-Message: Called "net usershare info" but it failed: Failed to execute child process “net” (No such file or directory)
```

Because Nautilus uses the `net usershare info` command to get information about non-root user defined [Samba](https://www.samba.org/) shares. In order to use `net`, the following package should be installed:

```console
# apt install samba-common-bin
```

And then I got the new error message:

```
Nautilus-Share-Message: Called "net usershare info" but it failed: 'net usershare' returned error 255: mkdir failed on directory /var/run/samba/msg.lock: Permission denied
net usershare: cannot open usershare directory /var/lib/samba/usershares. Error No such file or directory
Please ask your system administrator to enable user sharing.
```

Just create the directory as mentioned:

```console
# mkdir -p /var/lib/samba/usershares/
```
