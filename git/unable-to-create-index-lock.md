# Unable to create `index.lock`

For the error when trying to execute a `git` command:

```
Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.
```

Remove the existing `index.lock`:

```console
$ rm -f .git/index.lock
```
