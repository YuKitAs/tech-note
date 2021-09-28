# Squash Commits

Assuming we have three recent commits `A->B->C` on a local branch and we want to squash `B` and `C` into one single commit, run

```console
$ git checkout <branch>
$ git rebase -i master
```

In the interactive window we will see:

```
pick A <commit A>
pick B <commit B>
pick C <commit C>
```

To update the commit message we can use `squash`, if we want to use the commit message of the previous commit, we can use `fixup` (e.g. `C` fixes a typo in `B`) like:

```
pick A <commit A>
pick B <commit B>
fixup C <commit C>
```

We can also reorder the commits with the risk of raising conflicts, or cancle the rebase process with `git rebase --abort`.
