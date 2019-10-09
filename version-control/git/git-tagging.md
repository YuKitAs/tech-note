# Git Tagging

Tagging is often used to mark release points as being important, e.g. `v1.0`.

* Create a (lightweight) tag:

```console
$ git tag <tag-name>
```

* Create an annotated tag with a message:

```console
$ git tag -a <tag-name> -m "<message>"
$ git tag -m "<message>" <tag-name>
```

* Overwrite the message of an existing tag:

```console
$ git tag <tag-name> <tag-name>^{} -f -m "<new-message>"
```

* List all available tags:

```console
$ git tag
```

* List all tags that match a pattern:

```console
$ git tag -l <pattern>
```

* Show tag data with the commit:

```console
$ git show <tag-name>
```

* View a version pointed by a tag:

```console
$ git checkout <tag-name>
```

* Push a tag explicitly (By default, `git push` won't transfer tags to remote servers):

```console
$ git push origin <tag-name>
```

* Delete a remote tag:

```console
$ git push -d origin <tag-name>
```

* Delete a local tag:

```console
$ git tag -d <tag-name>
```

* Rename a tag:

```console
$ git tag <new-tag-name> <old-tag-name>
$ git tag -d <old-tag-name>
$ git push origin :refs/tags/<old-tag-name>
$ git push --tags
```
