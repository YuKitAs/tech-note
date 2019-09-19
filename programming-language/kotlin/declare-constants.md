# Declare Constants

Since Kotlin has no `static` keyword, there are basically two ways to declare constant in Kotlin.

1. Local constants on the top-level of the class file:

  ```kotlin
  private const val CONST_INT = 42
  private const val CONST_STRING = "Hello Bonbon"

  class MyClass {
  }
  ```

  It's equivalent to an immutable Java class with `static final` variables:

  ```java
  public final class MyClass {
    private static final int CONST_INT = 42;
    @NotNull
    private static final String CONST_STRING = "Hello Bonbon";
  }
  ```

2. Global constants in a companion object of a class or in an object:

  ```kotlin
  class MyConstants {
    companion object {
      const val CONST_INT = 42
      const val CONST_STRING = "Hello Bonbon"
    }
  }

  object MyConstants {
    const val CONST_INT = 42
    const val CONST_STRING = "Hello Bonbon"
  }
  ```

  The constants can be accessed globally as `MyConstants.CONST_INT` and `MyConstants.CONST_STRING`.

  The first one will be decompiled to the following Java class:

  ```java
  public final class MyConstants {  
    public static final int CONST_INT = 42;
    @NotNull
    public static final String CONST_STRING = "Hello Bonbon";
    public static final MyConstants.Companion Companion = new MyConstants.Companion((DefaultConstructorMarker)null);

    public static final class Companion {
      private Companion() {
      }

      // $FF: synthetic method
      public Companion(DefaultConstructorMarker $constructor_marker) {
        this();
      }
    }
  }
  ```

  The second one:

  ```java
  public final class MyConstants {
    public static final int CONST_INT = 42;
    @NotNull
    public static final String CONST_STRING = "Hello Bonbon";
    public static final MyConstants INSTANCE;

    static {
       MyConstants var0 = new MyConstants();
       INSTANCE = var0;
    }
  }
  ```
