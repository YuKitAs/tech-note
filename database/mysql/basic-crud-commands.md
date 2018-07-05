# Basic CRUD Commands

Insert a new record into table:

```console
mysql> INSERT INTO table_name (col1, col2, ...) VALUES (val1, val2, ...);
mysql> INSERT INTO table_name VALUES (val1, val2, ...);
```

Update a record:

```console
mysql> UPDATE table_name SET field1 = val1, field2 = val2, ... WHERE condition;
```

Delete a record from table:

```console
mysql> DELETE FROM table_name WHERE condition;
```

Delete all records from a table:

```console
mysql> TRUNCATE TABLE table_name;
```

If we intend to truncate a table that is referenced in a foreign key constraint, we can disable the constraint temporarily like:

```console
mysql> SET FOREIGN_KEY_CHECKS = 0;
/* truncating operations */
mysql> SET FOREIGN_KEY_CHECKS = 1;
```
