# Run MongoDB on Ubuntu

* Start MongoDB:

```console
sudo service mongod start
```

* Verify the status of MongoDB by checking the log file:

```console
cat /var/log/mongodb/mongod.log
```

If there is line reading `[initandlisten] waiting for connections on port <port>`, it means that MongoDB has started successfully. `<port>` is configured in `/etc/mongod.conf`, the default value is `27017`.

* Stop MongoDB:

```console
sudo service mongod stop
```

* Restart MongoDB:

```console
sudo service mongod restart
```
