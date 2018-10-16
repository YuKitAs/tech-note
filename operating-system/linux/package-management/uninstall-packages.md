# Uninstall Packages

`apt remove` is used to remove the package itself (the binaries).

`auto-remove` is used to remove any other dependencies for the package that were automatically installed.

`purge` is used to delete configuration and/or data files.

So the whole command to uninstall a package completely should be:

```console
$ sudo apt purge --auto-remove <package-name>
```

where `purge` is equivalent to `remove --purge`.
