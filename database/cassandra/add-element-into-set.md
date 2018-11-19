# Add Element into Set

For a non-empty field with type `set<text>`, the following command can be used to add new elements into the field:

```sql
UPDATE <table_name> SET <col_name> = <col_name> + {'new-value-1', 'new-value-2'} WHERE <condition>;
```
