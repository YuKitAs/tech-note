# Revert to a Previous Commit

In order to revert to a previous commit, copy commit hash from `git log`, and then run:

```console
git reset --hard <commit>
```

Revert to the most recent commit:

```console
git reset --hard HEAD
```
