# Basic Commands of `redis-cli`

* **List all keys**:

```
keys *
```

* **Set a simple key-value pair**:

```
SET <key> <value>
```

* **Get value by key**:

```
GET <key>
```

* **Set a hash with multiple fields and values**:

```
HSET <key> <field1> <value1> <field2> <value2> ...
```

* **Get the value of a single field**:

```
HGET <key> <field>
```

* **Get all fields/values by key:**

```
HGETALL <key>
```
