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

Secondary indexes are used to query a table using a column that is not normally queryable.

For example, partition keys `col_1` and `col_2` are defined when creating a table:

```
CREATE TABLE keyspace_name.table_name ( 
  col_1 int, 
  col_2 text, 
  col_3 int,
  PRIMARY KEY ((col_1, col_2), col_3) 
);
```

As a composite partition key, both `col_1` and `col_2` must be specified for a condition. So a secondary index must be created on `col_1` and `col_2`.

The secondary index can also be created on the clustering key `col_3`.

However, as the index table is stored on each node of the Cassandra cluster, secondary indexes can impact performance when accessing multiple nodes.
