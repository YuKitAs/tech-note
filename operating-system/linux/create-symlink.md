# Create Symlink

Create a symlink in `/usr/bin` which references to an executable in another directory:

```console
# ln -s /path/to/executable /usr/bin/command
```

Then we will get the symlink created in `/usr/bin/`:

```
lrwxrwxrwx  1 root root 23 Sep 23  2019 command -> /path/to/executable
```

Check the executable path of a symlink:

```console
$ ls -l $(which command)
```

Remove a symlink:

```console
# unlink /usr/bin/command
```
