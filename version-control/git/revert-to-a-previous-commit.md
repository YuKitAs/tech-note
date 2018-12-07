# Revert to a Previous Commit

## Hard reset

To give up committed changes and revert to a previous commit.

Copy commit hash from `git log` and then run:

```console
$ git reset --hard <commit>
```

Revert to the most recent commit:

```console
$ git reset --hard HEAD
```

In some situations like a branch is accidentally deleted, so that commit logs can not be accessed by `git log`, use `git reflog` to check all the local actions instead, and then do `git reset` as mentioned above.

## Soft reset

To undo commits but keep the changes e.g. when committed to a false branch.

In a similar way:

```console
$ git reset --soft <commit>
```
