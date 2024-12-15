# Basic Use of Date

The current date can be read by `date`.

Get with custom formatting like:

```console
$ date +"%Y-%m-%d %H:%M:%S"
```

Display the date in UTC:

```console
$ date -u
```

Display the date in a specific timezone like:

```console
$ TZ='Europe/London' date
```

Get the current timestamp in seconds since Unix epoch (can be used to compare timestamps):

```console
$ date +%s
```

Get the last modification timestamp of a file:

```console
$ date -r <file>
```
