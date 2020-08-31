# Java Collections


`Collection` is the root interface in the collection hierarchy (see [Java Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)). It provides implementations of subinterfaces like `Set`, `List`, `Queue` and extends `Iterable` interface with a default `stream()` method.

All the collection classes in the `java.util` package except `Vector` and `HashTable` are not thread-safe in order to maximize performance.


## Synchronized Collections

In multi-threaded context, synchronized collections can be generated as a wrapper:

```java
List<String> unsafeList = new ArrayList<>();
List<String> safeList = Collections.synchronizedList(unsafeList);
```

The synchronization mechanism uses the collection object itself as the lock object which will causes overhead and reduces performance.

## Concurrent Collections

Concurrent collections (since Java 5) provide better performance than synchronized collections with the following mechanisms:

1. `copy-on-write`: store values in an immutable array and create a new array when values need to be changed. For use cases when read operation greatly predominate write operations. Two implementations are `CopyOnWriteArrayList` and `CopyOnWriteArraySet`.

2. `compare-and-swap` (CAS): make a local copy of the variable and calculate the value, compare the value with its copy at the start before updating. Collections using CAS include `ConcurrentLinkedQueue` and `ConcurrentSkipListMap` (an implementation for `ConcurrentNavigableMap`).

3. using `java.util.concurrent.locks.Lock` (e.g. `ReentrantLock`): a `Lock` is held until its `unlock()` method is called. Collections using this lock include `ConcurrentHashMap` and most of the implementations of `BlockingQueue`.
