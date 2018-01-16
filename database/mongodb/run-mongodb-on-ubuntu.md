# Run MongoDB on Ubuntu

* Start MongoDB server:

```console
$ sudo service mongod start
```

* Verify the status of MongoDB by checking the log file:

```console
$ cat /var/log/mongodb/mongod.log
```

If there is line reading `[initandlisten] waiting for connections on port <port>`, it means that MongoDB has started successfully. `<port>` is configured in `/etc/mongod.conf`, the default value is `27017`.

* Stop MongoDB server:

```console
$ sudo service mongod stop
```

* Restart MongoDB server:

```console
$ sudo service mongod restart
```

* Start MongoDB client:

```console
$ mongo
```


* For detailed commands see documentation: [mongo Shell Quick Reference](https://docs.mongodb.com/manual/reference/mongo-shell/)
