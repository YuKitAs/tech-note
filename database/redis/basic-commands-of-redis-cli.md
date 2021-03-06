# Basic Commands of `redis-cli`

* **List all keys**:

```
KEYS *
```

* **Delete all keys in current database**:

```
FLUSHDB
```

* **Delete all keys in all databases**:

```
FLUSHALL
```

* **Set a simple key-value pair**:

```
SET <key> <value>
```

* **Check the type of value a key maps to**:

```
TYPE <key>
```

* **Get string value by key**:

```
GET <key>
```

* **Get set value by key**:

```
SMEMBERS <key>
```

* **Set a hash with multiple fields and values:**

```
HSET <key> <field1> <value1> <field2> <value2> ...
HMSET <key> <field1> <value1> <field2> <value2> ...
```

* **Get the value of a single field:**

```
HGET <key> <field>
```

* **Get values of multiple fields by key:**

```
HMGET <key> <field1> <field2> ...
```

* **Get all fields/values by key**:

```
HGETALL <key>
```

* **Switch to another database (0-15 by default)**:

```
SELECT <db_id>
```

* **Get the size (cardinality) of a set**:

```
SCARD <key>
```

* **Check memory usage of a stored value**:

```
MEMORY USAGE <key>
```

* **Check expiration of a key**:

```
TTL <key>
```
