# Merging and Rebasing

Both `git rebase` and `git merge` can be used to integrate changes from one branch into another. For example, to merge a new branch into the `master` branch:

**Merging**
```console
$ git checkout master
$ git pull
$ git merge <new-branch>
```

**Rebasing**

```console
$ git checkout master
$ git pull
$ git checkout <new-branch>
$ git pull
$ git rebase master
```

The major difference is, `merge` won't change the existing branches, while `rebase` will remove the entire new branch to `master`.

If we want the project history to be as clean as possible, it's better to use `rebase` instead of `merge`.

Since `git pull` is equivalent to `git fetch` followed by `git merge FETCH_HEAD`, when we have unpushed local commits and pull from a remote `master` branch without `--rebase`, what we are doing is actually merging the remote `master` into the local `master`, and this merge commit will be logged. So if we check the git branch graph (`git log --graph`) we would see something like this:

```
      *---*---* origin/master
     /         \
*---*---*---*---* master in local repo
```

If it's not wanted, we should always add `--rebase` in such a case.

## Interactive Rebasing

Futhermore, we can also use `rebase` to clean up a messy history before merging `new-branch` into `master` by adding the `-i` option:

```console
$ git rebase -i master
```

A list of commits will be shown in a text editor. We can then change the `pick` command and/or reorder the commits as we want. For example, if a commit only fixes a typo in another commit, we can condense them into a single commit by using `fixup` command.

## References

* [The Golden Rule of Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing), Bitbucket.
* [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), Git Documentation.
