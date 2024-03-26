# Git Debugging

There are some environment variables used for debugging, like `GIT_TRACE` for general traces for Git commands.

Either set the environment variable before the Git command like

```console
$ GIT_TRACE=1 git pull
```

or enable it by `export GIT_TRACE=1` and disable it with `export GIT_TRACE=0` afterwards.

## Reference

* [Git Internals - Environment Variables](https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables#Debugging)
