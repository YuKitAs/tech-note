# Basic Use of Grep

## Search for Multiple Patterns

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

## Show Lines Before and After

To search lines before (`-B`) and after (`-A`) match:

```console
$ grep -B<num> -A<num> <pattern> <file>
```

## Show First Match

```console
$ grep -m 1 <pattern> <file>
```

## Search in Compressed Files

Some log files are auto compressed in `gzip` format (`g` for GNU), to view, page and filter these files suffixed with `.gz`, use `zcat`, `zless` or `zgrep`.
