# Create and Apply Patch

* Create patch from local changes in working directory as well as staged files:

  ```console
  $ git diff HEAD > patch.diff
  ```

  Local changes only:

  ```console
  $ git diff > patch.diff
  ```

  Staged files only:

  ```console
  $ git diff --cached > patch.diff
  ```

* Apply the patch file:

  ```console
  $ git apply patch.diff
  ```
