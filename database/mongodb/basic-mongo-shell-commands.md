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

**Use a database (if the database does not exist, it will be created and used automatically)**:

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

**Delete a collection**:

```shell
db.<collection_name>.drop()
```

**Show all documents in a collection**:

```shell
db.<collection_name>.find()
```

**Show all documents in a collection prettily**:

```shell
db.<collection_name>.find().pretty()
```

**Insert a document to a collection**:

```shell
db.<collection_name>.insert({ <field>: <value> })
```

**Delete document(s) by a given condition**:

```shell
db.<collection_name>.deleteOne({ <field>: <value> })
db.<collection_name>.deleteMany({ <field>: <value> })
# Delete all documents in a collection
db.<collection_name>.deleteMany({})
db.<collection_name>.remove({})
```

## Reference

* [Mongo Shell Quick Reference](https://docs.mongodb.com/manual/reference/mongo-shell/)
