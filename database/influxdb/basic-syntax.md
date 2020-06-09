# Basic Syntax

* List databases and create/use a database:

  ```
  SHOW DATABASES
  CREATE DATABASE <db>
  USE <db>
  ```

* Insert a new data point (no space after `,`):

  ```
  INSERT <measurement>,<tag1-key>=<tag1-value>,<tag2-key>=<tag2-value> <field1-key>=<field1-value> [unix-nano-timestamp]
  ```

  where `tags` are indexed and `fields` are not.

* Query data (use single quotes for tag value):

  ```
  SELECT <tag1-key>, <field1-key> FROM <measurement> [WHERE <field1-key> condition AND <tag1-key>='<tag1-value>']
  ```

* Delete data/measurement:

  ```
  DELETE FROM <measurement> [WHERE <tag-key>='<tag-value>']
  DELETE FROM <measurement> [WHERE time condition]
  DROP <measurement>
  ```
 
 * Show human readable timestamp instead of epoch:

  ```
  > precision rfc3339
  ```
