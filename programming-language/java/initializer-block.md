# Initializer Block

## Static Initialization Blocks

In Java class, the `static initialization block` is a block including instructions that will be executed only once when the class is loaded into memory:

```java
class Whatever {
  static {
    // init class variables
  }
}
```

There can be multiple static blocks at any position in a class.

The alternative is to use a private static method like

```java
class Whatever {
  public static Var var = initSomething();

  private static Var initSomething() {
    // init var
  }
}
```

## Initializing Instance Members

The `instance initialization block` (IIB) is a block that will be executed before the constructors and every time an instance is created:

```java
class Whatever {
  {
    // init instance variables
  }
}
```

IIBs in the parent class will be executed before IIBs and constructors in the child class.

Alternative one is simply to initialize the instance variables with complex logic in the constructor.

Alternative two is to use a final method like

```java
class Whatever {
  private Val val = initSomething();

  private final Val initSomething() {
    // init var
  }
}
```

The Java compiler just copies initializer blocks into every constructor, so it can be used to share the code between multiple constructors (also think about if the Telescoping Constructor pattern will fit the needs).
