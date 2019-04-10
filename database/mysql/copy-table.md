# Copy Table

1. Copy table structure and indexes without data:

  ```sql
  CREATE TABLE new_table LIKE old_table;
  ```

2. Copy table structure and data without indexes:

  ```sql
  CREATE TABLE new_table SELECT * FROM old_table;
  ```

3. Copy everything:

  ```sql
  CREATE TABLE new_table LIKE old_table;
  INSERT new_table SELECT * FROM old_table;
  ```
