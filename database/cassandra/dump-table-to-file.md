# Dump Table to File

1. `csv` as the default format regardless of the filename extension:

  ```
  cqlsh> COPY <keyspace.table> [(<col>, ...)] TO <file> WITH [<option>='<value>'];
  ```

  Available options for tuning the output are: `DELIMITER` (default: `,`), `QUOTE` (default: `"`), `ESCAPE` (default: `\`), `HEADER` (default: `false`), `ENCODING` (default: `utf8`), `NULL` (default: empty string).

  Example:

  ```
  cqlsh> COPY default.users (id, username, email) TO './users.dat' WITH DELIMITER = ' ' AND NULL = 'null';
  ```

  Output of `users.dat`:

  ```
  0 foo foo@bar.com
  1 bar null
  ```

2. `txt` as the default format (same as the CQL output with `|` as delimiter):

  ```console
  $ cqlsh -k <keyspace> -e 'SELECT * FROM <table>' > <file>
  ```

  Example:

  ```console
  $ cqlsh -k default -e 'SELECT id, username, email FROM users' > ./users.dat
  ```

  Output of `users.dat`:

  ```
  id| username | email
  --+----------+-------------
  0 |      foo | foo@bar.com
  1 |      bar |        null
  ```
