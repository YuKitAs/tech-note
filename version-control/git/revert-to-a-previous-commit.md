# Revert to a Previous Commit

## Hard reset

To give up committed changes and revert to a previous commit.

Copy the unwanted commit hash from `git log` and then run:

```console
$ git reset --hard <commit>
```

Undo the most recent commit:

```console
$ git reset --hard HEAD~1
```

`~1` means up one level in the hierarchy.

In some situations like a branch is accidentally deleted, so that commit logs can not be accessed by `git log`, use `git reflog` to check all the local actions instead, and then do `git reset` as mentioned above.

## Soft reset

To undo commits but keep the changes e.g. when committed to a false branch.

In a similar way (`--soft` is the default option though):

```console
$ git reset --soft <commit>
```

Undo the most recent commit:

```console
$ git reset HEAD~1
```
