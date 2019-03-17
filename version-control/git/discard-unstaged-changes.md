# Discard Unstaged Changes

For all unstaged files (reset path):

```console
$ git checkout -- .
```

`--` is used here to avoid disambiguation by indicating the following argument `.` is a path instead of a branch.

For a single file:

```console
$ git checkout <filename>
```
