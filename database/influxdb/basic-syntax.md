# Basic Syntax

* List databases and create/use a database:

  ```
  SHOW DATABASES
  CREATE DATABASE <db>
  USE <db>
  ```

* Insert a new data point:

  ```
  INSERT <measurement>,<tag1-key>=<tag1-value>,<tag2-key>=<tag2-value> <field1-key>=<field1-value> [unix-nano-timestamp]
  ```

  where `tags` are indexed and `fields` are not.

* Query data:

  ```
  SELECT <tag1-key>, <tag2-key>, <field1-key> FROM <measurement> [WHERE <field1-key> condition]
  ```

* Delete data/measurement:

  ```
  DELETE FROM <measurement> [WHERE <tag-key>="<tag-value>"]
  DELETE FROM <measurement> [WHERE time condition]
  DROP <measurement>
  ```
