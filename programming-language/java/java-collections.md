# Java Collections

`Collection` is the root interface in the collection hierarchy (see [Java Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)). It provides implementations of subinterfaces like `Set`, `List`, `Queue` and extends `Iterable` interface with a default `stream()` method.

The main differences between some common implementations are listed as follows (`SortedSet` is a subtype of `Set`):

| Implementation       | {ordered} | {unique} |
| -------------------  | --------- | -------- |
| java.util.Collection |    no     |    no    |
| java.util.Set        |    no     |    yes   |
| java.util.List       |    yes    |    no    |
| java.util.SortedSet  |    yes    |    yes   |
