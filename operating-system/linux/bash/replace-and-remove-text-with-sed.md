# Replace and Remove Text with `sed`


* Replace all occurrence of a pattern (globally with `g`):

```console
$ sed 's/pattern/new_pattern/g' <file>
```

Example:

```console
$ echo "Hello world!" | sed 's/Hello/Goodbye/'
```

Remove a directory `/home/wrong/bin` from `PATH`:

```console
$ export PATH=`echo $PATH | sed -e 's/:\/home\/wrong\/bin//'`
```

* Delete the n-th line, last line, lines from x to y:

```console
$ sed 'nd' <file>
$ sed '$d' <file>
$ sed 'x,yd' <file>
```

* Delete line matching pattern:

```console
$ sed '/pattern/d' <file>
```
