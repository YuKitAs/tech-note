# Java Collections

`Collection` is the root interface in the collection hierarchy (see [Java Documentation]((https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)). It provides implementations of subinterfaces like `Set` and `List`. `SortedSet` is a subinterface of `Set`.

The main differences between them are listed as follows:

| Implementation       | {ordered} | {unique} |
| -------------------  | --------- | -------- |
| java.util.Collection |    no     |    no    |
| java.util.Set        |    no     |    yes   |
| java.util.List       |    yes    |    no    |
| java.util.SortedSet  |    yes    |    yes   |
