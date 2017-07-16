# CountDownLatch

CountDownLatch is a synchronization aid that allows one or more threads to wait until a set of operations being performed in other threads completes.

The implementation of `CountDownLatch` with methods `await()` and `countDown()`:

```java
public class CountDownLatch {
    private int count;

    public CountDownLatch(int count) {
        this.count = count;
    }

    public void await() throws InterruptedException {
        synchronized (this) {
            while (count > 0) {
                this.wait();
            }
        }
    }

    public void countDown() {
        synchronized (this) {
            if (count > 0) {
                count--;
                if (count == 0) {
                    this.notifyAll();
                }
            }
        }
    }
}
```

The implementation of `Worker` thread using `CountDownLatch`:

```java
public class Worker implements Runnable {
    private CountDownLatch countDownLatch;

    public Worker(CountDownLatch countDownLatch) {
        this.countDownLatch = countDownLatch;
    }

    @Override
    public void run() {
        doSomeWork();
        countDownLatch.countDown();
    }

    public void doSomeWork() {}
}
```
