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

* Checkout an unmerged branch (for review):

  ```console
  $ git fetch origin
  $ git checkout -b <branch-name> origin/<branch-name>
  ```

For merging and rebasing see [note](https://github.com/YuKitAs/tech-note/blob/master/version-control/git/git-merge-and-git-rebase.md).
