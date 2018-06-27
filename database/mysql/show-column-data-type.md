# Show Column Data Type

* Show columns including `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`:

```sql
mysql> SHOW COLUMNS from <db_name>.<table_name>;
```

* Show the table schema:

```sql
mysql> DESCRIBE <db_name>.<table_name>;
mysql> DESC <db_name>.<table_name>;
```

* Show the SQL statement that can be used to create a table:

```sql
mysql> SHOW CREATE TABLE <db_name>.<table_name>;
```

* Use the `information_schema_columns`:

```sql
mysql> SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '<table_name>' AND COLUMN_NAME = '<column_name>';
```
