# Revert to a Previous Commit

## Hard reset

To give up committed changes and revert to a previous commit.

Copy the commit hash that should be kept from `git log` and then run:

```console
$ git reset --hard <commit>
```

The HEAD will be reset to this commit, means all the commits after this one will be gone.

Undo the most recent commit:

```console
$ git reset --hard HEAD~
```

`HEAD~` is shorthand for `HEAD~1`, pointing to the previous commit of the most recent one.

In some situations like a branch is accidentally deleted, so that commit logs can not be accessed by `git log`, use `git reflog` to check all the local actions instead, and then do `git reset` as mentioned above.

## Soft reset

To undo commits but keep the changes e.g. when committed to a false branch.

In a similar way (`--soft` is the default option though):

```console
$ git reset --soft <commit>
```

Undo the most recent commit:

```console
$ git reset HEAD~
```
