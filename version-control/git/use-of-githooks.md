# Use of Githooks

Githooks are executable programs that can trigger actions at certain points in Git's execution. They can be used to automate development workflow. For example, the hook `prepare-commit-msg` will be invoked by Git after preparing the default log message and before the commit message editor is opened.

To use githooks, we need to place the hooks in a directory, say, `~/.githooks` and make the hook files executable. Then specify the path with:

```console
$ git config --global core.hooksPath ~/.githooks
```


## Reference

* [Git Documentation](https://git-scm.com/docs/githooks)
