# Set Connect and Request Timeout With `cqlsh`

The default timeout for connecting Cassandra with `cqlsh` is 5 seconds and for requesting dataset is 10 seconds. Larger timeouts can be specified on starting `cqlsh` like:

```
cqlsh --connect-timeout=1000 --request-timeout=6000
```
