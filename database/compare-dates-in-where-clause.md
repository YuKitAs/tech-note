# Compare Dates in WHERE Clause

The easiest way is to use comparison operators directly, like:
```console
WHERE date > CURDATE();
WHERE date < '2012-12-12';
```
Another way is to use `DATEDIFF()` function, which returns the difference of two date or date-and-time expressions (only the date parts will be calculated though). The above conditions can also be written as:
```console
WHERE DATEDIFF(date, CURDATE()) > 0;
WHERE DATEDIFF(date, '2012-12-12') <= -1;
```
