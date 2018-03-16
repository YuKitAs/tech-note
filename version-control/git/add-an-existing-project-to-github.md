# Add an Existing Project to GitHub

1. Create a new repo on GitHub (without README.md and LICENSE)

2. Initialize the local project as a Git repo:

    ```console
    $ git init
    ```

3. Add the URL for the new repo on GitHub, for example:

    ```console
    $ git remote add origin https://github.com/YuKitAs/[new-repo-name].git
    ```

4. Push changes in the local repo to GitHub (commit local changes or stash local changes and pull from the new repo before if necessary):

    ```console
    $ git push -u origin master
    ```
