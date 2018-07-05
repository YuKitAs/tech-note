# Show MySQL Query Output in Vertical Mode

When `sometable` has too many fields it will be hard to line up column titles with field values in the terminal.

Then we can display the output in vertical mode using `\G` to execute the query instead of `;`:

```sql
mysql> SELECT * FROM sometable \G
```
