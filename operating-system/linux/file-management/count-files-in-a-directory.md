# Count Files in a Directory

To count all the files and directories (except `.*`) in the current directory:

```console
$ ls -1 | wc -l
```

To *recursively* list all files in a directory, we can use `find` with specified type `f`:

```console
$ find <dir> -type f | wc -l
```

To exclude a directory:

```console
$ find <dir> -type f -not -path "./<excluded-dir>/*" | wc -l
```
