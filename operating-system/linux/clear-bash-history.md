# Clear Bash Histroy

The file storing command history can be found with:

```console
$ echo $HISTFILE
```

By default it's `~/.bash_history`. The number of commands that can be stored is set in `~/.bashrc`, like `HISTSIZE=1000`.

The following command clears the temporary history for the current session:

```console
$ history -c
```

An easy way to wipe out the content in `.bash_history`:

```console
$ <whitespace> > ~/.bash_history
```
