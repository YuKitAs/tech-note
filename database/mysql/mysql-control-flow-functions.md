# MySQL Control-Flow-Functions

`CASE` statement is used to apply a conditional construct. For example:

```sql
UPDATE table_name SET col_name = 
CASE
WHEN condition1 THEN value1
WHEN condition2 THEN value2
...
ELSE value_else
END;
```

`IF()` function returns a value based on `TRUE` or `FALSE` condition.
It takes 3 expressions. If `expr_condition` is `TRUE`, non zero and not `NULL`, `expr_true` will be returned, otherwise `expr_false` will be returned:

```sql
SELECT IF(expr_condition, expr_true, expr_false) FROM table_name;
```

`IFNULL()` function takes 2 expressions. `expr1` will be returned if it's not `NULL`, otherwise `expr2` will be returned:

```sql
SELECT IFNULL(expr1, expr2) FROM table_name;
```

`NULLIF()` function takes 2 expressions. It returns `NULL` when both expressions are equal, otherwise the first expression will be returned.
