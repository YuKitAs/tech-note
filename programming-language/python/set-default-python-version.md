# Set Default Python Version

Use `update-alternatives` to set Python version with priorities:

```
update-alternatives --install <link> <name> <path> <priority>
```

For example:

```console
# update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
# update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
```

The bigger number indicates the higher priority.

Check currently configured alternatives:

```console
# update-alternatives --config python
```

Check default Python version:

```console
$ python -V
Python 3.8.2
```
