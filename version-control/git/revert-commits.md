# Revert to a Previous Commit

## `git-reset`

Reset current branch HEAD to the specified state. As opposed to `git add`, it can be used to reverse added files from staging area to working directory. To reverse committed files, there are different modes to choose, like `--soft`, `--mixed` or `--hard`. The default mode is `--mixed`, which means resetting commits and keeping the changes as "Untracked files".

### Soft reset

To undo commits but keep the changes in the staging area as "Changes to be committed":

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

* Revert some existing commits and generate commits with messages stating which commits were reverted:

  ```console
  $ git revert <commit>
  ```

* Revert commits without generating commit messages:

  ```console
  $ git revert -n <commit>
  ```

* Revert merged commits:

  ```console
  $ git revert -m 1 <merge_commit>
  ```

  The `-m` option specifies the parent number of the merge commit.

## Revert master to a previous tag

  ```console
  $ git checkout <tag>
  $ git diff master > ~/diff.patch
  $ git checkout master
  $ git apply ~/diff.patch
  ```
