# Check SQL Mode

Verify the current SQL mode by executing:

```conolse
# mysql -e "SELECT @@sql_mode;"
```

When `STRICT_TRANS_TABLES` is present, it means the Strict Mode is enabled.
