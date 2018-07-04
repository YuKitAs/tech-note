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

Create a new user:

```console
$ mysql> CREATE USER <username>@localhost IDENTIFIED BY <password>;
```

Grant a user with all rights:

```console
$ mysql> GRANT ALL PRIVILEGES ON *.* TO <username>@localhost IDENTIFIED BY <password>;
```
