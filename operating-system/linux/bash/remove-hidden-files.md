# Remove Hidden Files

To remove all the files/directories including hidden files/directories in the current directory, there are several simple options:

```console
$ rm -rf * .*
$ rm $(ls -A)
$ ls -A | xargs rm -rf
$ find ! -name '.' ! -name '..' -delete
```

Normally, the `.` and `..` directories won't be deleted by `rm` and thus we will get warnings like

```
rm: refusing to remove '.' or '..' directory: skipping '.'
rm: refusing to remove '.' or '..' directory: skipping '..'
```

To be safer, we could also use the following patterns to exclude `.` and `..` explicitly:

```console
$ rm -rf ..?* .[!.]* *
```

A tricky way is to enable `dotglob` and then disable it after deletion:

```console
$ shopt -s dotglob
$ rm -rf *
$ shopt -u dotglob
```
