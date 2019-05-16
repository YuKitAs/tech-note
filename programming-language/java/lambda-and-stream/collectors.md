# Collectors

In Java 8, `Stream.collect()` allows to perform mutable fold operations on data elements in a stream instance. Some common `Collectors` methods are `toList()`, `toMap()` and `groupingBy()`, `minBy()/maxBy()`, `joining()`. They are preferred to `forEach()` because `forEach()` should only be used to present the result computed by a stream.

An example of using `toList()`:

```java
List<Integer> integers = Stream.of(11, 10, 7, 12, 3).sorted().limit(3).collect(Collectors.toList());
integers.forEach(System.out::println);
```

Output:
```
3
7
10
```

`toMap()` can take two functions which map a stream element to a key and a value, for example:

```java
List<String> strings = List.of("custom", "random", "word", "generator"); // since Java 9

Map<String, Integer> words = strings.stream().collect(Collectors.toMap(Function.identity(), String::length));
words.forEach((k, v) -> System.out.println(k + ": " + v));
```

Output:
```
random: 6
custom: 6
generator: 9
word: 4
```

`groupingBy()` can take a classifier and returns a map of elements that are grouped by some property:

```java
Map<Integer, Set<String>> groupedWords = strings.stream().collect(Collectors.groupingBy(String::length, Collectors.toSet()));
groupedWords.forEach((k, v) -> System.out.println(k + ": " + v));
```

Output:
```
4: [word]
6: [random, custom]
9: [generator]
```

`partitioningBy()` can take a predicate and split the elements into `Map<Boolean, List<T>>`:

```java
Map<Boolean, List<String>> partitionedStrings = strings.stream().collect(Collectors.partitioningBy(s -> s.length() < 5));
System.out.println(partitionedStrings.get(true));
```

Outout:
```
[word]
```
