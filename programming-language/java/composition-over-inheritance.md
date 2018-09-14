# Composition over Inheritance

Composition over inheritance is a principle of OOP that classes should achieve polymorphic behavior and code reuse by containing references to an instance of other class rather than inheriting from a parent class, the reason is that inheritance violates encapsulation and could lead to fragility in subclasses as the subclasses need to depend on the implementation details of its superclass.

For example, instead of extending an implementation of `Set<E>`, the following forwarding class is designed to be reusable and can be extended by a decorator class:

```java
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> set;

    public ForwardingSet(Set<E> set) {
        this.set = set;
    }

    @Override
    public boolean add(E e) {
        return set.add(e);
    }

    @Override
    public boolean remove(Object o) {
        return set.remove(o);
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        return set.addAll(c);
    }

    ...
}
```

The decorator class with new implementations:

```java
public class WrapperSet<E> extends ForwardingSet<E> {
  public WrapperSet(Set<E> set) {
      super(set);
  }

  @Override
  public boolean add(E e) {
    ...
    return super.add(e);
  }

  ...
}
```

Passing a `Set` instance to the wrapper like:

```java
Set<Integer> s = new WrapperSet<>(new HashSet<>());
```
