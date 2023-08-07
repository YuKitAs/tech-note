# Rename Multiple Files

Use the Perl command `rename` with regex to rename multiple files based on a pattern.

For example, rename the followings files
```
1-foo.txt
2-bar.txt
```
to
```
foo-1.txt
bar-2.txt
```
with
```bash
$ rename -n 's/(\d)-(\w+).txt/$2-$1.txt/' *
rename(1-foo.txt, foo-1.txt)
rename(2-bar.txt, bar-2.txt)
```
`-n` (`--no-act`) is used to test the regex first without actually renaming the files.
