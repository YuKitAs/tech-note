# Set Default Ruby Version

Add the following into `~/.bashrc`:

```
source $HOME/.rvm/scripts/rvm
```

Use `rvm` to list installed Ruby versions:

```console
$ rvm ls
```

Choose a default version, for example:

```
$ rvm --default use 2.7.1
```
