# Queries on Set

## Add element into set

For a non-empty field with type `set<text>`, the following command can be used to add new elements into the field:

```sql
UPDATE <table_name> SET <col_name> = <col_name> + {'new-value-1', 'new-value-2'} WHERE <condition>;
```

## Filter by element in set

```sql
SELECT <col_name> FROM <table_name> WHERE <col_name> CONTAINS 'value';
```
