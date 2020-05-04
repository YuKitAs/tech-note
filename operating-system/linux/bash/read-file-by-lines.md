# Read File by Lines

Read the first X lines:

```console
$ head -n X <file>
```

Read the last X lines:

```console
$ tail -n X <file>
```

Read starting from line X:

```console
$ tail -n +X <file>
```

Read from line N to line M (starting at line N):

```console
$ tail -n +N <file> | head -n (M - N + 1)
```
