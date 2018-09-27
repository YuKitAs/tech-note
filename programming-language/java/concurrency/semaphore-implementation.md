# Semaphore Implementation

Semaphore is another synchronization mechanism like monitor, but at lower level. It's a thread synchronization construct that can be used to send signals between threads. Since Java 5, a semaphore implementation is provided in package `java.util.concurrent`.

 Below is an example of a semaphore with an upper bound (capacity).

```java
public class SemaphoreDemo {
    private int tickets;
    private final int capacity;

    public SemaphoreDemo(int capacity, int tickets) {
        assert (capacity > 0 && tickets >= 0);

        this.capacity = capacity;
        this.tickets = tickets;
    }

    public synchronized void acquire() throws InterruptedException {
        while (tickets == 0) wait();

        tickets--;
        notifyAll();
    }

    public synchronized void release() throws InterruptedException {
        while (tickets == capacity) wait();

        tickets++;
        notifyAll();
    }
}
```
