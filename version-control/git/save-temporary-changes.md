# Save Temporary Changes

1. To save uncommitted local changes:
  
  ```console
  $ git stash
  ```
  It's equivalent to `git stash push`.

  The stash entries can be listed with `git stash list` and the changes stored in a stash entry can be shown with `git stash show [stash-entry]`.

2. Pull from remote `master` without creating a separate branch:
  
  ```console
  $ git pull --rebase
  ```

3. Re-apply the stashed changes to the working branch:
  
  ```console
  $ git stash apply [stash-entry]
  ```
  or
  ```console
  $ git stash pop [stash-entry]
  ```
  The difference between `apply` and `pop` is whether the changes would be kept in stash or removed.

  All the stash entries can be removed with 

  ```console
  $ git stash clear
  ```
  
  A single stash entry can be removed with 

  ```console
  $ git drop [stash-entry]
  ```
  
  So actually, `stash pop` is the combination of `stash apply` and `stash drop`. 
