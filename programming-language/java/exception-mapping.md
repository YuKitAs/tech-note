# Exception Mapping

In the Java world, `RuntimeException` stands for exceptions that would be thrown during the runtime of the JVM. They are so-called unchecked exceptions that don't need to be declared. In some occasions, say, we don't want to deal with any interruptions, we can map the checked exception to an unchecked exception.

The following example illustrates how to map a checked exception (here an `InterruptedException`) to `RuntimeException` with customized error message.

Firstly, define a `CustomException` class which extends `RuntimeException`:

```java
public class CustomException extends RuntimeException {
    private static final String INTERRUPTED_ERROR_MESSAGE = "Thread is interrupted";

    private CustomException(String message, Throwable cause) {
        super(message, cause);
    }

    public static CustomException forInterrupted(InterruptedException cause) {
        return new CustomException(INTERRUPTED_ERROR_MESSAGE, cause);
    }
}
```

Then we can catch the `InterruptedException` and throw a new `CustomException` like this:

```java
try {
    /* some operations that would raise InterruptedException */
} catch (InterruptedException e) {
    throw CustomException.forInterrupted(e);
}
```
