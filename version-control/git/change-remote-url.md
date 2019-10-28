# Change Remote URL

Existing remotes can be listed by `git remote -v`:

```console
origin	git@github.com:YuKitAs/tech-note.git (fetch)
origin	git@github.com:YuKitAs/tech-note.git (push)
```

If we have renamed a remote repo, we can change the fetch remote to make the local repo point to the new URL:

```console
$ git remote set-url origin <new-remote-url>
```

If we have a forked repo and set the fetch remote as the original repo, we can change the push remote separately:

```console
$ git remote set-url --push origin <forked-repo-url>
```
