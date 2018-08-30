# Enum with Constant Specific Body

The following example shows how to define constant-specific body for each enum:

```java
public enum Pokemon {
    PIKACHU {
        public String getType() {
            return "Electric";
        }
    }, CHARMANDER {
        public String getType() {
            return "Fire";
        }
    }, MEOWTH {
        public String getType() {
            return "Normal";
        }
    };

    public abstract String getType();
}
```

Another way is to use constructor (which is implicitly private):

```java
public enum Pokemon {
    PIKACHU("Electric"), CHARMANDER("Fire"), MEOWTH("Normal");

    private final String type;

    Pokemon(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }
}
```

For function object fields, we can use constructor to store lambdas in an instance field (with the help of functional interfaces). For example:

```java
public enum Pokemon {
    PIKACHU(() -> "Electric"), CHARMANDER(() -> "Fire"), MEOWTH(() -> "Normal");

    private final Supplier<String> type;

    Pokemon(Supplier<String> type) {
        this.type = type;
    }

    public String getType() {
        return type.get();
    }
}
```
