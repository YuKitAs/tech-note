# `git-merge` and `git-rebase`

Both `git rebase` and `git merge` can be used to integrate changes from one branch into another. For example, usual ways to merge the `master` branch into a feature branch:

```console
$ git checkout master
$ git pull --rebase
$ git checkout <feature-branch>
$ git merge [-Xours|-Xtheirs] master
```

The `-Xours|-Xtheirs` option is used to overwrite conflicts, `-Xours` means the changes in the feature branch will overwrite master.

A major difference is, `merge` won't change the existing branches, while `rebase` will remove the entire new branch to `master` without generating a merge commit.

If we want the project history to be as clean as possible, it's better to use `rebase` instead of `merge`.

Since `git pull` is equivalent to `git fetch` followed by `git merge FETCH_HEAD`, when we have unpushed local commits and pull from a remote `master` branch without `--rebase`, what we are doing is actually merging the remote `master` into the local `master`, and this merge commit will be logged. So if we check the git branch graph (`git log --graph`) we would see something like this:

```
      *---*---* origin/master
     /         \
*---*---*---*---* master in local repo
```

If it's not wanted, we should always add `--rebase` in such a case.

## Interactive Rebasing

Furthermore, we can also use `rebase` to clean up a messy history before merging `new-branch` into `master` by adding the `-i` option:

```console
$ git rebase -i master
```

or for certain number of commits:

```console
$ git rebase -i HEAD~3
```

A list of commits will be shown in a text editor. We can then change the `pick` command and/or reorder the commits as we want. For example, if a commit only fixes a typo in another commit, we can condense them into a single commit by using `fixup`/`f` command.

## References

* [The Golden Rule of Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing), Bitbucket.
* [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), Git Documentation.
