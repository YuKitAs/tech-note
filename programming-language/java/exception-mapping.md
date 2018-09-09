# Exception Mapping

In the Java world, `RuntimeException` stands for exceptions that would be thrown during the runtime of the JVM. They are so-called unchecked exceptions that don't need to be declared. Unlike checked exceptions which are generally used for recoverable conditions (the method caller should handle the exception), unchecked exceptions should be used to indicate programming errors.

In some occasions where we don't want to deal with a checked exception, we can also map it to an unchecked exception.

In the following example, the checked exception class `InterruptedException` will be wrapped into a subclass of `RuntimeException` with customized error message.

Firstly, create a `CustomException` class which extends `RuntimeException`, define a static constructor and pass the `InterruptedException` as the `cause` parameter:

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

However, if additional information like error message is not necessary, we can only return an empty `Optional` of the desired type to avoid throwing a checked exception.
