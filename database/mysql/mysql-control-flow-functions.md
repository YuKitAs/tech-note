# MySQL Control-Flow-Functions

`CASE` statement is used to apply a conditional construct:

```console
SELECT
CASE
WHEN expr_condition1 THEN result1
WHEN expr_condition2 THEN result2
...
ELSE result_else
END
FROM sometable;
```

`IF()` function returns a value based on `TRUE` or `FALSE` condition.
It takes 3 expressions. If `expr_condition` is `TRUE`, non zero and not `NULL`, `expr_true` will be returned, otherwise `expr_false` will be returned:
```console
SELECT IF(expr_condition, expr_true, expr_false) FROM sometable;
```

`IFNULL()` function takes 2 expressions. `expr1` will be returned if it's not `NULL`, otherwise `expr2` will be returned:
```console
SELECT IFNULL(expr1, expr2) FROM sometable;
```

`NULLIF()` function takes 2 expressions. It returns `NULL` when both expressions are equal, otherwise the first expression will be returned.
