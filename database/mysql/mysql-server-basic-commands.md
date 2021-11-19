# MySQL Server Basic Commands

Start/stop/restart MySQL Server:

```console
# service mysql start
# service mysql stop
# service mysql restart
```

Check server status:

```console
# service mysql status
```

Login as root (and use a database):

```console
$ mysql -u root -p<password> [db_name]
```

Create a new user:

```sql
mysql> CREATE USER <username>@localhost IDENTIFIED BY <password>;
```

Grant a user with all rights:

```sql
mysql> GRANT ALL PRIVILEGES ON *.* TO <username>@'localhost' [IDENTIFIED BY <password>];
```

Show user rights:

```sql
mysql> SHOW GRANTS [FOR <username>];
