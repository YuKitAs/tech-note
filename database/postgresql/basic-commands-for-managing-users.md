# Basic Commands for Managing Users

* **Create a new user from shell (switch to the superuser `postgres` first)**:

  ```console
  $ su - postgres
  $ createuser <username>
  ```

* **List all existing users (roles)**:

  ```sql
  SELECT usename FROM pg_user;
  ```

* **View all permissions of existing users**:

  ```console
  postgres=# \du
  ```

* **Set password**:

  ```console
  postgres=# \password <username>
  ```

* **Grant permissions (`CREATEDB`, `CREATEROLE`, `CREATEUSER`, `SUPERUSER` etc.)**:

  ```sql
  ALTER USER <username> WITH <PERMISSION1> <PERMISSION2> ...;
  ```
  
  For Grafana:
  
  ```sql
  GRANT SELECT ON <table> TO <username>;
  ```

* **Revoke permissions**:

  ```sql
  ALTER USER <username> WITH <NOPERMISSION1> <NOPERMISSION2> ...;
  ```
