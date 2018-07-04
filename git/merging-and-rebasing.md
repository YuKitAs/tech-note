# Merging and Rebasing

Both `git rebase` and `git merge` can be used to integrate changes from one branch into another, like:

```console
$ git checkout <new-branch>
$ git rebase master
```

or

```console
$ git merge master <new-branch>
```

However, the major difference is, merging doesn't change the existing branches, the `new-branch` will have a merge commit every time when there is a new change in `master`, so the branch history of `new-branch` would not be so clear to understand. Rebasing moves the entire `new-branch` to `master` and rewrites the project history.

Interactive rebasing is used to clean up a messy history before merging `new-branch` into `master`:

```console
$ git checkout <new-branch>
$ git rebase -i master
```

A list of commits will be shown in a text editor. We can then change the `pick` command and/or reorder the commits as we want.

## References

* [The Golden Rule of Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing), Bitbucket.

* [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), Git Documentation.
