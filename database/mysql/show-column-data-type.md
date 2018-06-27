# Show Column Data Type

* Use the `information_schema_columns`:

```sql
mysql> SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '<table_name>' AND COLUMN_NAME = '<column_name>';
```

* Show the table schema including `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`:

```sql
mysql> describe <db_name>.<table_name>;
mysql> desc <db_name>.<table_name>;
```

* Show the SQL statement that can be used to create a table:

```sql
mysql> show create table <db_name>.<table_name>;
```
