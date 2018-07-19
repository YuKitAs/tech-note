# Count Files in a Directory

To recursively list all files in a directory, we can use `find` with specified type like:

```console
$ find <dir> -type f
```

Then we can use `wc -l` (short for `word count lines`) to count newlines.

So the whole command would be:

```console
$ find <dir> -type f | wc -l
```

If we want to exclude a directory, we can try

```console
$ find <dir> -type f -not -path "./<excluded-dir>/*" | wc -l
```
