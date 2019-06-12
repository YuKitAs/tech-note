# Grep Multiple Patterns

To search lines containing either `foo` or `bar`:

```console
$ egrep "foo|bar" <file>
$ grep -e foo -e bar <file>
```
