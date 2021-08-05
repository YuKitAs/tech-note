# Split File by Lines

```console
$ split [options] <filename> [<prefix>]
```

Default size is 1000 lines for each file, default prefix is "x", default suffix is "aa", "ab", etc.

For example, `test-file` has 1900 lines, by default we will get:

```
xaa # 1000 lines
xab # 900 lines
```

If we want to split it into 4 files of the same size, with custom prefix and numeric suffix, we can use:

```console
$ split -l 475 -d test-file file
```

now we will get:

```
file01
file02
file03
file04
```
