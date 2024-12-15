# Directory Stack

Some useful Bash commands to manipulate a list of recently-visited directories:

* Push a directory to the stack and navigate to it:

```console
$ pushd <dir>
```

For example:

```console
~$ pushd dir1
~/dir1 ~
~/dir1$ pushd dir2
~/dir1/dir2 ~/dir1 ~
```

* List directories in the stack:

```console
$ dirs -v
0  ~/dir1/dir2
1  ~/dir1
2  ~
```

The 0 directory is always the current directory.

* Navigate to a directory in the stack:

```console
$ cd ~2
```

* Return to the last directory in the stack:

```console
$ popd
```

* Clear directory stack:

```console
$ dirs -c
```
