# MySQL JOIN

In standard SQL, the different types of JOINs are:

1. **(INNER) JOIN**: returns records that match the `WHERE` clause in both tables
2. **LEFT (OUTER) JOIN**: returns all records from the left table and matched records from the right table
3. **RIGHT (OUTER) JOIN**: returns all records from the right table and matched records from the left table
4. **FULL (OUTER) JOIN**: returns all records that match in either left or right table
5. **CROSS JOIN**: returns a Cartesian product of two tables (no `ON` clause)

In MySQL, **JOIN** is syntactically equivalent to **INNER JOIN** and **CROSS JOIN**, they can replace each other. If `WHERE` clause is used with **CROSS JOIN**, it functions like an **INNER JOIN** with `ON` clause.

## Reference

* [MySQL 8.0 Reference Manual - JOIN Syntax](https://dev.mysql.com/doc/refman/8.0/en/join.html)
