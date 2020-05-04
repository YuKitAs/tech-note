# Read File by Lines

Read the first N lines:

```console
$ head -n N <file>
```

Read the last M lines:

```console
$ tail -n M <file>
```

Read starting from line X:

```console
$ tail -n +X <file>
```

Read from line N to line M (starting at line N):

```console
$ tail -n +N <file> | head -n (M - N + 1)
```
