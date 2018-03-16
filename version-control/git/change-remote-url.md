# Change Remote URL

Using HTTPs, a remote repository URL might look like this:

```console
https://github.com/<username>/<repo-name>.git
```

If we want to push the current project to another repository, we need to change the remote URL using the following command:

```console
git remote set-url origin <new-remote-url>
```

Existing remotes can be listed by `git remote -v`.
