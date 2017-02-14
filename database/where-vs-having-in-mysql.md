# WHERE vs HAVING in MySQL

`WHERE` filters data before `SELECT`, thus putting the condition in `WHERE` clause will be more efficient.

`HAVING` is applied after `GROUP BY` and can filter data on aggregates like `SUM(value)`. MySQL also allows referencing aliases in `HAVING`. For example:
```console
SELECT value AS v FROM sometable WHERE v > 0;
```
This will cause "Unknown column" error. But it works well with `HAVING` clause:
```console
SELECT value AS v FROM sometable HAVING v > 0;
```
By the way, a trick of using aliases in `WHERE` is to use subquery in `FROM` clause like:
```console
SELECT v FROM (SELECT value AS v FROM sometable WHERE v > 0) AS q;
```
It is useful when the column definition is complicated.
