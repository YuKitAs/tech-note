# Git Branch Basics

* Create a new branch (track a remote branch) and switch to it:

```console
$ git checkout -b <new-branch>
```

* Delete a fully merged branch:

```console
$ git branch -d <branch-name>
```

* Delete a (not fully merged) branch:

```console
$ git branch -D <branch-name>
```

* Push to a branch:

```console
$ git push -u origin <branch-name>
```

* Push to the current branch:

```console
$ git push -u origin HEAD
```
