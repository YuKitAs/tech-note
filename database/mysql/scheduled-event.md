# Scheduled Event

Syntax:
```sql
CREATE EVENT [IF NOT EXIST] <event_name>
ON SCHEDULE <schedule>
DO
<event_body>
```

Example:
```sql
CREATE EVENT IF NOT EXISTS ClearHistory
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM history WHERE created < NOW() - INTERVAL 1 YEAR;
```
