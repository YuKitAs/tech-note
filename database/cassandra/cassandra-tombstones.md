# Cassandra Tombstones

Tombstones in Cassandra are soft-deleted cells which would cause performace issues when the number grows big. Tombstones are generated not only by simple `DELETE` statements, but also by the following operations:

1. Inserting null values: Cassandra does not read data to check existence before writing
2. Inserting into or updating collection columns
3. Expiring data with TTL
4. Deleting with full primary key will generate tombstones that are not traceable in the logs or counted in metrics. 
