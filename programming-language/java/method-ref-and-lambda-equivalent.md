# Method References and Lambda Equivalent

| | Method Ref | Lambda Equivalent |
|-| ---------- | ----------------- |
|Static|`Integer::sum`|`(x, y) -> x + y`|
|Bound|`Instant.now()::isAfter`|`t -> Instant.now().isAfter(t)`|
|Unbound|`String::toUpperCase`|`str -> str.toUpperCase()`|
|Class Constructor|`HashMap<K,V>::new`|`() -> new HashMap<K,V>()`|
|Array Constructor|`int[]::new`|`n -> new int[n]`|
