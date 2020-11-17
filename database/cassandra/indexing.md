# Indexing

## Define Index

Create an index on a column:

```sql
CREATE INDEX [index_name] ON keyspace_name.table_name (column_name);
```

Index `set` and `list` collections:

```sql
CREATE INDEX [index_name] ON keyspace_name.table_name (collection_column);
SELECT * FROM keyspace_name.table_name WHERE collection_column CONTAINS some_value;
```

Index `map` collections:

```sql
CREATE INDEX [index_name] ON keyspace_name.table_name ( KEYS (map_column) );
SELECT * From keyspace_name.table_name WHERE map_column CONTAINS KEY some_key;
```

The `index_name` is optional. When not specified, Cassandra will name it `table_name_column_name_idx` by default.

## Secondary Index
