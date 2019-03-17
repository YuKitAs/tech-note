# Change Remote URL

If we have renamed a remote repo, we can make the local repo point to the new URL with the following command:

```console
$ git remote set-url origin <new-remote-url>
```

Existing remotes can be listed by `git remote -v`, for example:

```console
origin	git@github.com:YuKitAs/tech-note.git (fetch)
origin	git@github.com:YuKitAs/tech-note.git (push)
```
