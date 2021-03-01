# Show Foreign Key Constraints

Show all foreign key constraint names:
```sql
SELECT CONSTRAINT_NAME FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
WHERE CONSTRAINT_TYPE = 'FOREIGN KEY' AND TABLE_NAME = '<table_name>';
```

Show all foreign key constraints with referenced tables and columns:
```sql
SELECT
  TABLE_NAME,
  COLUMN_NAME,
  CONSTRAINT_NAME,
  REFERENCED_TABLE_NAME,
  REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
  REFERENCED_TABLE_NAME = '<table_name>';
```
