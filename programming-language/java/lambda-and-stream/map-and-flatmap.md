# `map` and `flatMap`

As its name indicates, `flatMap()` is used to avoid nested structures when using `map()`.

For example, `Stream.of(Arrays.asList(1, 2), Arrays.asList(3, 4)).collect(Collectors.toList())` will return `[[1, 2], [3, 4]]` with type `List<List<Integer>>`. If we want to get `[1, 2, 3, 4]` we have to use `flatMap()` as follows:

```java
List<Integer> result = Stream.of(Arrays.asList(1, 2), Arrays.asList(3, 4))
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
```
