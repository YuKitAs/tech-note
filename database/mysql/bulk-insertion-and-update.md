# Bulk Insertion and Update

Insert multiple rows with one query:

```sql
INSERT INTO my_table (id, name) VALUES (0, 'foo'), (1, 'bar');
```

Update multiple rows with one query:

```sql
UPDATE my_table SET name = (CASE id WHEN 0 THEN 'baz' WHEN 1 THEN 'qux' END) WHERE id IN (0, 1);
```

Attention, in the following case, the update query would violate the unique constraint on `name`:

```sql
UPDATE my_table SET name = (CASE id WHEN 0 THEN 'bar' WHEN 1 THEN 'foo' END) WHERE id IN (0, 1);
```
