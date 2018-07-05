# MySQL Server Time Zone

By default, when the MySQL server starts, it will use the time zone of the host machine to set the `system_time_zone` variable.

The global `time_zone` variable indicates the time zone the server is currently operating in, the initial value is `SYSTEM`. We can use the following command to check the server time zone value (together with the session time zone value):

```sql
mysql> SELECT @@global.time_zone, @@session.time_zone;
```

And we can check the current server time with:

```sql
mysql> SELECT CURRENT_TIMESTAMP();
mysql> SELECT NOW();
```

The time zone values can be set at runtime with `SUPER` privilege:

```sql
mysql> SET GLOBAL time_zone = timezone; /* server time zone */
mysql> SET time_zone = timezone; /* session time zone */
```

This value can either be a string indicating an offset from UTC such as  `'+00:00'` or a named time zone if the time zone information tables have been created and populated.

## Reference

* [MySQL Server Time Zone Support](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html), MySQL 5.5 Reference Manual
