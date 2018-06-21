# Show Column Data Type

Use the `information_schema_columns`:

```sql
SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '<table_name>' AND COLUMN_NAME = '<column_name>';
```
