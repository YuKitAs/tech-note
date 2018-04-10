# Search for Debian Packages

Use `dpkg --list` and `grep` to search for Debian packages by a regex pattern of the package name:

```console
$ dpkg -l | grep <regex>
```
