# Merging and Rebasing

Both `git rebase` and `git merge` can be used to integrate changes from one branch into another.

**Merging**
```console
$ git merge master <new-branch>
```
**Rebasing**

```console
$ git checkout <new-branch>
$ git rebase master
```



The major difference is, `merge` won't change the existing branches, here the `new-branch`, while `rebase` will remove the entire `new-branch` to `master`.

If we want the project history to be as clean as possible, it's better to use `rebase` instead of `merge`.

## Interactive Rebasing

Futhermore, we can also use `rebase` to clean up a messy history before merging `new-branch` into `master` by adding the `-i` option:

```console
$ git checkout <new-branch>
$ git rebase -i master
```

A list of commits will be shown in a text editor. We can then change the `pick` command and/or reorder the commits as we want. For example, if a commit only fixes a typo in another commit, we can condense them into a single commit by using `fixup` command.

## References

* [The Golden Rule of Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing), Bitbucket.
* [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), Git Documentation.
