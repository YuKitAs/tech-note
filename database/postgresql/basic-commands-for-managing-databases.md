# Basic Commands for Managing Databases

* **Connect to a database as a user from shell with `psql`**:

  ```console
  $ psql <db_name> <username>
  ```

* **Create a database for a user**:

  ```console
  postgres=# CREATE DATABASE <db_name> OWNER <username>;
  ```
  
* **List all databases**:

  ```console
  postgres=# \l
  ```

* **Switch to another database as current user**:

  ```console
  postgres=# \c <db_name>
  ```
  
* **Switch to another database as another user**:

  ```console
  postgres=# \c <db_name> <username>
  ```

* **List all tables in the current database**:

  ```console
  postgres=# \dt
  ```

* **Describe a table**:

  ```console
  postgres=# \d <table_name>
  ```
* **Dump a table**:

  ```console
  pg_dump -st <table_name> <db_name>
  ```

* **Set timezone**:

  ```sql
  SET TIME ZONE <timezone_name>;
  SHOW TIMEZONE;
  ```
  
* **List triggers**:

  ```sql
  SELECT * FROM information_schema.triggers;
  ```

* **List enum type**:

  ```sql
  SELECT enum_range(NULL::<enum_name>);
  ```
  
* **Add a new value to enum**:

  ```sql
  ALTER TYPE <enum_name> ADD VALUE '<new_value>';
  ```
