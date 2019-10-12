# Revert to a Previous Commit

## `git-reset`

Reset current branch HEAD to the specified commit. The default mode is `--mixed`.

### Soft reset

To undo commits but keep the changes e.g. when committed to a false branch (but not pushed):

```console
$ git reset --soft <commit>
```

Undo the most recent commit:

```console
$ git reset HEAD~
```
where `HEAD~` is shorthand for `HEAD~1`, pointing to the previous commit of the most recent one.


### Hard reset

To give up committed changes and revert to a previous commit:

```console
$ git reset --hard <commit>
```

In some situations like a branch is accidentally deleted, so that commit logs can not be accessed by `git log`, use `git reflog` to check all the local actions instead, and then do `git reset` as mentioned above.

## `git-revert`

Revert some existing commits and generate commits with messages stating which commits were reverted:

```
$ git revert <commit>
```
