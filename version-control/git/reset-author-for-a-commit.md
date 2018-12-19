# Reset Author for a Commit

In case we committed with a default committer by accident, and then configured the correct committer with `git config` before pushing, we have the chance to reset the committer with:

```console
$ git commit --amend --reset-author
```
