# Sync Two Directories

Copy all the content of `dir1` to `dir2`:

```console
$ rsync -av --progress dir1/ dir2
```

Copy all the content of `dir1` to `dir2`, and delete files from `dir2` which are not contained in `dir1`:

```console
$ rsync -av --progress --delete dir1/ dir2
```
