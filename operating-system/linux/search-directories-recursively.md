# Search Directories Recursively

[`ripgrep`](https://github.com/BurntSushi/ripgrep) is a useful tool to search directories recursively based on regex patterns (and it's said to be [faster than everything else](https://blog.burntsushi.net/ripgrep/)).

`rg` will ignore hidden and binary files by default.

A most simple use-case is to search in all files case-insensitively:

```console
$ rg -uu -i <pattern>
```
