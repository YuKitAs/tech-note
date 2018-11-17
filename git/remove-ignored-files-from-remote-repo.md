# Remove Ignored Files from Remote Repo

Sometimes we want to add some files into `.gitignore` after they are already pushed to the remote repo, to remove these ignored files, usually we will have to remove all the files in the local repo (remember to commit local changes first) and then add them back so that the new rules in `.gitignore` can be applied:

```console
$ git rm -rf --cached .
$ git add .
$ git commit -m "Remove files that should be ignored"
$ git push origin master
```
