# `tee` Command

`tee` (named after T-splitter) is used to redirect standard input to both standard output and specified file(s), primarily with pipes and filters, like:

```console
$ echo "Hello world" | tee hello.txt
$ ls -l | tee files.txt | grep hello
```

The optional flag `-a` can be used to append the content to file(s) instead of overwriting it.
