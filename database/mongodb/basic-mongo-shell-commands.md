# Basic Mongo Shell Commands

**Enter Mongodb**:

```console
$ mongo
```

**Leave Mongodb**:

```shell
exit
```

**Show all databases**:

```shell
show dbs
```

**Use a database**:

```shell
use <db_name>
```

**Show all collections**:

```shell
show collections
```

**Create a collection**:

```shell
db.createCollection("<collection_name>")
```

**Show all documents in a collection**:

```shell
db.<collection_name>.find()
```

**Insert a document to a collection**:

```shell
db.<collection_name>.insert({ <field>: <value> })
```

**Delete document(s)**:

```shell
db.<collection_name>.deleteOne({ <field>: <value> })
db.<collection_name>.deleteMany({ <field>: <value> })
```

## Reference

* [Mongo Shell Quick Reference](https://docs.mongodb.com/manual/reference/mongo-shell/)
