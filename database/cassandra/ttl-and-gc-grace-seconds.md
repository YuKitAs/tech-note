# TTL and `gc_grace_seconds`

## Column TTL
In Cassandra, `INSERT` and `UPDATE` command support setting TTL (precision is one second) for one or multiple columns. With CQL:

```sql
INSERT INTO <table> (<col_1>, <col_2>, ...) VALUES (<value_1>, <value_2>, ...) USING TTL 86400;
UPDATE <table> USING TTL 259200 SET <col> = <value> WHERE <condition>;
```

The element in a collection can have individual TTL.

After expiration, the columns will have NULL values.

Query TTL for a column:

```sql
SELECT ttl(<col>) FROM <table> WHERE <condition>;
```

Getting TTL for primary keys and collections (set, list and map) are not supported by `ttl()` function.

## Table TTL
The table TTL can be set with the table property `default_time_to_live`. The default value is 0, which means table TTL is disabled.

Change table TTL with CQL:

```sql
ALTER TABLE <table> WITH default_time_to_live = 864000;
```

After expiration, the table will be tombstoned.

## `gc_grace_seconds`
`gc_grace_seconds` is a table property which decides when the data marked with a tombstone (a deletion marker) should be garbage collected. The default value is 864000 seconds (10 days). It can be reduced when tables only contain data with TTL set or with `default_time_to_live` set.
