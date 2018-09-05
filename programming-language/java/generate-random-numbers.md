# Generate Random Numbers

The most common way to generate random numbers within a given range was to use the standard library `java.util.Random`. For example, generating integers from 1 to 10 (plus 1 because the upper bound 10 is exclusive):

```java
int number = new Random().nextInt(10) + 1;
```

`Random` is thread safe, but if the same instance of `Random` is used by multiple threads, the same seed will be shared and thus lead to poor performance in multi-threaded environment.

Since Java 7, consider using `java.util.concurrent.ThreadLocalRandom` which has a `Random` instance per thread and produces higher quality random numbers fast:

```java
int number = ThreadLocalRandom.current().nextInt(10) + 1;
```
