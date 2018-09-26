# Clear Bash Histroy

The file storing command history can be found with:

```console
$ echo $HISTFILE
```

By default it's `~/.bash_history`.

The following command clears the history for the current session:

```console
$ history -c
```

An easy way to wipe out the content in `.bash_history`:

```console
$ <whitespace> > ~/.bash_history
```
