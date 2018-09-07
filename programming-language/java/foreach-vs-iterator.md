# `Foreach` vs `Iterator`

The `for-each` loop is the preferred idiom to iterate over a collection or array:

```java
for (Foo foo : fooList) {
  // do something with `foo`
}
```

for nested iteration:

```java
for (Foo foo : fooList) {
  for (Bar bar : barList) {
    // do something with `foo` and `bar`
  }
}
```

An `Iterator` will be used when destructive filtering is needed (e.g. removing an element from the collection), there are usually two ways - using a `for` loop or `while` loop.

`for` loop:
```java
for (Iterator<Foo> i = list.iterator(); i.hasNext(); ) {
  Foo foo = i.next();
  // do something with `i` and `foo`
}
```

`while` loop:
```java
Iterator<Foo> i = list.iterator();
while (i.hasNext()) {
  doSomething(i.next());
}
```

The `for` loop is preferable to the `while` loop, because the scope of local variable `i` in the `for` loop is smaller.
