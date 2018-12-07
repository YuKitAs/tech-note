# Overwrite Remote Branch

Git force push is used to overwrite a remote branch with local changes. The following commands are equivalent when forcefully pushing a branch to remote:

```console
$ git push -f origin <branch>
```
or
```console
$ git push origin +<branch>
```
