# MySQL User Management

Create a new user:

```sql
mysql> CREATE USER <username>@localhost IDENTIFIED BY <password>;
```

Grant a user with all rights:

```sql
mysql> GRANT ALL [PRIVILEGES] ON *.* TO '<username>'@'localhost' [IDENTIFIED BY <password>];
```

Show all rights for current user or a specific user:

```sql
mysql> SHOW GRANTS [FOR <username>];
