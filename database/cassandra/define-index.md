# Define Index

Create an index on a column:

```sql
CREATE INDEX [index_name] ON keyspace_name.table_name (column_name);
```

The `index_name` is optional. When not specified, Cassandra will name it `table_name_column_name_idx` by default.
