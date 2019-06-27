# Redis Data Types

The basic Redis data types are:
* **String**: the most basic type. Binary safe.
* **List**: collections of strings sorted in the order of insertion. It's possible to push new element either to the head (left) or tail (right). Linked lists.
* **Set**: unordered collections of unique strings. Adding, removing and checking existence in O(1). No need to check existence before adding new element. It's possible to do unions, intersections or differences.
* **Sorted set**: every member is associated with a score (a chosen field) for sorting. Often used to index data. Ranges can be got by score or by position (rank).
* **Hash**: maps between string fields and string values. Takes little space to store millions of objects.

Every list, set or hash can store up to 2^32 - 1 (more than 4 billion) members.

## Reference
* [An introduction to Redis data types and abstractions](https://redis.io/topics/data-types-intro)
