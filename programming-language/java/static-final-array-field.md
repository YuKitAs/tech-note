# Static Final Array Field

In Java, a non-empty array is mutable, that means, if a class has a public static final array field or an accessor that returns a reference to such a private array field, the contents of the array can be modified. There are two ways to fix the potential security problem.

1. Returns a copy of the private array:

  ```java
  private static final Foo[] ARRAY_VALUES = { ... };
  public static final Foo[] values() {
      return ARRAY_VALUES.clone();
  }
  ```

2. Converting the private array filed to a public immutable list:

  ```java
  private static final Foo[] ARRAY_VALUES = { ... };
  public static final List<Foo> VALUES = Collections.unmodifiableList(Arrays.asList(ARRAY_VALUES));
  ```
