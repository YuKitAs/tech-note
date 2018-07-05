# Compare Dates in WHERE Clause

The easiest way is to use comparison operators directly, like:
```sql
WHERE date > CURDATE();
WHERE date < '2012-12-12';
```
Another way is to use `DATEDIFF()` function, which returns the difference of two date or date-and-time expressions (only the date parts will be calculated though). The above conditions can also be written as:
```sql
WHERE DATEDIFF(date, CURDATE()) > 0;
WHERE DATEDIFF(date, '2012-12-12') <= -1;
```
If `date` is stored as a UNIX timestamp, we can use `FROM_UNIXTIME()` function to reformat it.
