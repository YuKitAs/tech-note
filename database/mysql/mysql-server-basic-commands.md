# MySQL Server Basic Commands

Start/stop/restart MySQL Server:

```console
$ service mysql start
$ service mysql stop
$ service mysql restart
```

Check server status:

```console
$ service mysql status
```

Login as root:

```console
$ mysql -u root -p
```

Create a new user with all rights:

```console
$ GRANT ALL PRIVILEGES ON *.* TO '<username>'@'localhost' IDENTIFIED BY '<password>';
```
