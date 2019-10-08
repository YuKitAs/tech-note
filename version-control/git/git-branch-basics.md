# Git Branch Basics

For merging and rebasing see [note](https://github.com/YuKitAs/tech-note/blob/master/version-control/git/git-merge-and-git-rebase.md).

* Create a new branch (track a remote branch) and switch to it:

  ```console
  $ git checkout -b <new-branch>
  ```

* Delete a fully merged branch locally:

  ```console
  $ git branch -d <branch-name>
  ```

* Delete a (not fully merged) branch locally:

  ```console
  $ git branch -D <branch-name>
  ```

* Push to a remote branch:

  ```console
  $ git push -u origin <branch-name>
  ```

  `-u` is shorthand for `--set-upstream`, which will set up an upstream reference and only needs to be specified once for the first time. Ever after, `git push` can be used to push to `origin/<current-branch-name>` automatically.

* Push to a remote branch from the current branch:

  ```console
  $ git push -u origin HEAD
  ```

  `HEAD` should be used only when the HEAD is pointing to the last commit in the current branch (check with `git log`).

* Rename a branch:

  ```console
  $ git branch -m <old-name> <new-name>
  ```

* Rename the current branch:

  ```console
  $ git branch -m <new-name>
  ```

* Delete the remote branch with old name and push the local branch with new name (`master` branch cannot be deleted):

  ```console
  $ git push origin :<old-name> <new-name>
  ```

* Checkout a remote branch:

  ```console
  $ git fetch <remote>
  $ git checkout <branch-name>
  ```

* Compare another branch with the current branch:

  ```console
  $ git diff <another-branch>...
  ```

* List all remote branches:

  ```console
  $ git branch -r
  ```
  
* Show currently checked out branch:

  ```console
  $ git branch | grep \* | cut -d ' ' -f2
  ```
  Or
  ```console
  $ git rev-parse --abbrev-ref HEAD
  ```
