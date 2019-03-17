# Tracking Branches

Tracking branches are local branches that track a remote branch which is called "upstream branch". When cloning a repo, Git automatically creates a `master` branch to track `origin/master`, so that we can use `git pull` to fetch changes from `origin/master` and merge them into the local `master` branch.

A common case to track from other remotes is to use:

```console
$ git checkout -b <branch> <remote>/<branch>
```

It has a shortcut if the branch name exactly matches a remote one:

```console
$ git checkout <branch>
```

If the branch name doesn't exist, Git will automatically create a tracking branch.

For a fork repo (downstream repo), it's commonly needed to track the changes from the original repo, which should be added to the `upstream` remote:

```console
$ git remote add upstream <original-repo>.git
```

Fetch the changes from the `master` branch of the upstream repo and merge to local branch with:

```console
$ git fetch upstream
$ git merge upstream/master
```

or

```console
$ git pull upstream master
```
