# Add an Existing Project to Remote

1. Create a new repo with Git repo manager like GitHub or GitLab.

2. For a local project, initialize it to a Git repo:

    ```console
    $ git init
    ```

    As the default name of the remote repo is "origin", if the local project is already an existing Git repo and we don't want to reinitialize it, we need to change the current remote name to avoid conflict later, e.g. rename it as "old-origin":

    ```console
    $ git remote rename origin old-origin
    ```

3. Add the remote repo URL to remote `origin`:

    ```console
    $ git remote add origin <new-repo>.git
    ```

4. If there are uncommitted local changes, add and commit. For the fresh initialized repo, just use:

    ```console
    $ git push -u origin master
    ```

    For an existing Git repo with multiple branches, use:

    ```console
    $ git push -u origin --all
    $ git push -u origin --tags
    ```
