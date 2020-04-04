# Grep Multiple Patterns

To search lines containing `foo` OR `bar`:

```console
$ egrep "foo|bar" <file>
$ grep -E "foo|bar" <file>
$ grep "foo\|bar" <file>
$ grep -e foo -e bar <file>
```

To search lines containing `foo` AND `bar` (in any order):

```console
$ grep -E "foo.*bar|bar.*foo" <file>
$ grep "foo" <file> | grep "bar"
```
