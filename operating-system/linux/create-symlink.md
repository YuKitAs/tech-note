# Create Symlink

Create a symlink in `/usr/bin` which references to an executable in another directory (use absolute paths):

```console
# ln -s /path/to/executable /usr/bin/executable
```

Then we will get the symlink created in `/usr/bin/`:

```
lrwxrwxrwx  1 root root 23 Sep 23  2019 executable -> /path/to/executable
```

Remove a symlink:

```console
# unlink /usr/bin/executable
```
