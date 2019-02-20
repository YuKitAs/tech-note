# Cast `null`

The `null` can be cast to any reference type. A use case is when a method is overloaded:

```java
public void foo(String s) {
  // do sth with string
}

public void foo(Integer i) {
  // do sth with integer
}
```

If passing `null` to the method `foo()`, we need to cast it to a specific type explicitly like:

```java
foo((String) null);
foo((Integer) null);
```
