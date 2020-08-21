# Volatile and Atomic Variables

A typical example that won't work as expected in a multi-threading environment is:

```java
private int i;

public int increment(){
   return i++;
}
```

Since the operation `i++` does one read and one write without synchronization, another thread may write to `i` between the read and the write (race condition), thus it's unsafe.

Reads and writes are atomic for referenced variables and most primitive variables except `long` and `double`, and for variables that are declared with `volatile` keyword.

`volatile` keyword guarantees the value of the volatile variable will be read from main memory instead of from thread's local cache. It means, the volatile value may change every time, so that threads will automatically see the most up-to-date value.

Using volatile variables is considered simpler but fragiler than locking.

If we use `volatile int i` instead in the above example, all the threads will read the latest value of `i`, but the race condition is still there, because `volatile` only deals with visibility, but won't make the operation `i++` atomic.

The atomic variable classes (like `AtomicInteger` and `AtomicReference`) extend the concept of volatile variables and use `Compare-and-swap (CAS)` to achieve synchronization. The above example can be modified to a thread-safe version by using `AtomicInteger` like:

```java
private AtomicInteger i;

public int increment(){
   return i.getAndIncrement(); // Atomically increments by one the current value
}
```

## Reference

* [Managing volatility](https://www.ibm.com/developerworks/java/library/j-jtp06197/index.html). IBM, 2007.
