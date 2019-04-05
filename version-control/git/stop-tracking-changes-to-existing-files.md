# Stop Tracking Changes to Existing Files

When files have already been committed but any further changes are supposed to be ignored:

```console
$ git update-index --assume-unchanged <file>
```

Resume to track changes:

```console
$ git update-index --no-assume-unchanged <file>
```
