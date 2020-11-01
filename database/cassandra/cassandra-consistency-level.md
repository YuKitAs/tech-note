# Cassandra Consistency Level

Cassandra is a AP system according to the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) that provides high availability and partition tolerance, but the data in a replica can become inconsistent. It uses [repair operations](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/operations/opsRepairNodesTOC.html) to correct the inconsistencies and ensure all nodes have the same and most up-to-date data eventually.

The consistency level is configurable in Cassandra, there's a trade-off between operation latency and consistency. The consistency level determined how many replicas have to respond to a read or write request before the operation is considered successful.

Strong consistency can be guaranteed when the following condition is true:

```
R + W > N
```

where
* R: consistency level of read
* W: consistency level of write
* N: number of replicas

A common practice is to read and write at consistency level of QUORUM, which is calculated and rounded down as:

```
quorum = (sum_of_replication_factors / 2) + 1
```

`sum_of_replication_factors` is the sum of all replication factors for each datacenter.

For example, if the replication factor of a single datacenter is 3, a quorum is 2 nodes, the cluster can tolerate 1 replica down.

## References

* [Data consistency](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlAboutDataConsistency.html), DataStax Documentation for Apache Cassandra 3.0

* [CQL CONSISTENCY](https://docs.datastax.com/en/cql-oss/3.x/cql/cql_reference/cqlshConsistency.html), DataStax Documentation for CQL 3.x
