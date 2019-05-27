# Search Directories Recursively

[`ripgrep`](https://github.com/BurntSushi/ripgrep) is a useful tool to search directories recursively based on regex patterns (and it's said to be [faster than everything else](https://blog.burntsushi.net/ripgrep/), e.g. `fgrep`).

`rg` will ignore hidden and binary files by default, e.g. `.git`.

A most simple use-case is to search in all files (`uu`) case-insensitively (`-i`):

```console
$ rg -uu -i <pattern>
```
