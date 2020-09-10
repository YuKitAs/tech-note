# Delete From Select

The intuitive query would be something like:

```sql
DELETE FROM <table> WHERE id IN (
  SELECT id FROM <table> WHERE <condition>
);
```

However, this won't work because in MySQL, "you cannot update a table and select directly from the same table in a subquery".

A workaround is as follows:

```sql
DELETE FROM <table> WHERE id IN (
    SELECT * FROM (
        SELECT id FROM <table> WHERE <condition>
    ) AS c
);
```
