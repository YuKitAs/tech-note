# Execute SQL File

Using UNIX console:

```console
mysql -u<username> -p<password> <db_name> < path/to/file.sql
```

Using MySQL shell:

```
mysql> use <db_name>;
mysql> source path/to/file.sql
```

Export query result:

```console
$ mysql -u<username> -p<password> <db_name> < path/to/file.sql > output.txt
```

The exported columns are tab-separated by default.
