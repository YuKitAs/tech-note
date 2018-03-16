# Revert to a Previous Commit

In order to revert to a previous commit, copy commit hash from `git log`, and then run:

```console
git reset --hard <commit>
```

Revert to the most recent commit:

```console
git reset --hard HEAD
```

In some situations like a branch is accidentally deleted, so that commit logs can not be accessible by `git log`, use `git reflog` to check all the local actions instead, and then do `git reset` as mentioned above.
