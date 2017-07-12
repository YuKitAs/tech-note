# Wait And Notify

### wait
`wait()` method is called to suspend the current thread, it has three variants. The invocation of `wait()` will not return until any other thread has called `notify()` or `notifyAll()` on the object. The current thread suspended by `wait(long timeout)` will also be awakened when a specified amount of time has elapsed. The current thread suspended by `wait(long timeout, int nanos)` will also be awakened when some other thread interrupts it.

### notify
`notify()` method wakes up only one thread waiting on the object's monitor. The Choice of the thread is arbitrary (depends on the OS implementation of thread management).

### notifyAll
`notifyAll()` method wakes up all the threads waiting on the object's monitor. The awakened threads will not be able to proceed until the current thread relinquishes the lock on this object.

___
Here is an example to show how these methods actually work. Firstly we define an object class `Message`:

```java
public class Message {
    private String msg;

    public Message(String msg) {
        this.msg = msg;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
}
```

Then the `Waiter` and `Notifier` classes which implement `Runnable`:

```java
public class Waiter implements Runnable {
    private Message message;

    public Waiter(Message message) {
        this.message = message;
    }

    @Override
    public void run() {
        String name = Thread.currentThread().getName();

        synchronized (message) {
            try {
                System.out.println(name + " thread is waiting to get notified at time: " + System.currentTimeMillis());
                message.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(name + " thread got notified at time: " + System.currentTimeMillis());

            System.out.println(name + " thread has been processed: " + message.getMsg());
        }
    }
}

public class Notifier implements Runnable {
    private Message message;

    public Notifier(Message message) {
        this.message = message;
    }

    @Override
    public void run() {
        String name = Thread.currentThread().getName();
        System.out.println(name + " thread is started.");

        try {
            Thread.sleep(1000);
            synchronized (message) {
                message.setMsg(name + " has notified.");
                message.notify();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

Finally we create two `Waiter` threads and let them wait until the `Notifier` thread has called `notify()`. We would get the following output:

```
Waiter1 thread is waiting to get notified at time: 1499902253221
Waiter2 thread is waiting to get notified at time: 1499902253223
Notifier thread is started.
Waiter1 thread got notified at time: 1499902254224
Waiter1 thread has been processed: Notifier has notified.
```

Only one of the `Waiter` thread got notified. If we replace `notify()` with `notifyAll()` in `Notify`, the output would then be like:

```
Waiter1 thread is waiting to get notified at time: 1499902298896
Waiter2 thread is waiting to get notified at time: 1499902298897
Notifier thread is started.
Waiter2 thread got notified at time: 1499902299898
Waiter2 thread has been processed: Notifier has notified.
Waiter1 thread got notified at time: 1499902299898
Waiter1 thread has been processed: Notifier has notified.
```

It shows both threads got notified.
