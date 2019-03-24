# Export and Import Database

Exporting user and database:

```console
# pg_dump -U <username> <database> > /path/to/dbexport.pgsql
```

Importing database (the user must exist):

```console
# psql -U <username> <database> < /path/to/dbexport.pgsql
```
