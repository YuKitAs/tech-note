# Base64 Encode and Decode

To encode a string **without** appending a newline, use the following command:

```console
$ echo -n "Hello world" | base64 -w 0
SGVsbG8gd29ybGQ=
```

To decode a string, type `base64 -d` and press enter, type the text to decode, press enter again and `Ctrl + D`:

```console
$ base64 -d
SGVsbG8gd29ybGQ=
Hello world
```
