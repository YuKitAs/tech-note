# Basic Commands for Managing Databases

* **Create a database for a user**:

  ```sql
  CREATE DATABASE <db_name> OWNER <username>;
  ```

* **Connect to a database as a user from shell with `psql`**:

  ```console
  $ psql <db_name> <username>
  ```

* **Switch to another database as current user**:

  ```console
  postgres=# \c <db_name>
  ```

* **List all tables in the current database**:

  ```console
  postgres=# \dt
  ```

* **Describe a table**:

  ```console
  postgres=# \d <table_name>
  ```