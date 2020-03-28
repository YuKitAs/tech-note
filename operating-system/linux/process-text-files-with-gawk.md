# Process Text Files with `gawk`

Gawk is the GNU Project's implementation of the [AWK](https://en.wikipedia.org/wiki/AWK) programming language.

It's useful for processing large text files consisting one or multiple rows with fields separated by the same separator, like

```
foo 23  foo@gmail.com
bar 42  bar@hotmail.com
baz 16  NULL
```

The default field separators in a row are whitespace sequences (spaces, TABs, and newlines).

## Common Use Cases

* Select specific columns:

  ```console
  $ awk '{print $1,$2}' input.txt
  foo foo@gmail.com
  bar bar@hotmail.com
  ```

* Filter rows based on column values:

  ```console
  $ awk '$2 > 40 && $3 != NULL {print $1}' input.txt
  bar
  ```

* Parse another field separator, e.g. for `csv` files:

  ```console
  $ echo 'a,b,c' | awk -F, '{print $1,$2,$3}'
  a b c
  ```

## Reference

* [4.5.1 Whitespace Normally Separates Fields](https://www.gnu.org/software/gawk/manual/html_node/Default-Field-Splitting.html#Default-Field-Splitting), GNU
