# Sort Listed Directory Contents

## Sort by Directory/File Name

By default, the `ls` command lists directory contents by directory/file name alphabetically in ascending order. To sort in descending order, use `-r` (`--reverse`):

```console
$ ls -r
```

## Sort by Last Modification Time

```console
$ ll -t
$ ll -tr
```

## Sort by Directory/File Size (space usage on disk)

Although `ls` has `-s` (`--size`) option to sort by file size, the directory size it lists is actually the size of the meta information for the directory, so it's more reasonable to use `du` command combined with `sort`. The following commands list the directory/file size in human readable format:

```console
$ du -sh * | sort -h
$ du -sh * | sort -hr
```
