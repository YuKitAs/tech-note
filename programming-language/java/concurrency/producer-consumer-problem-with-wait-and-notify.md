# Producer-Consumer Problem with Wait and Notify

Here is an example for the implementation of Producer-Consumer Problem using [wait and notify](https://github.com/YuKitAs/tech-note/blob/master/programming-language/java/concurrency/wait-and-notify.md) instead of `BlockingQueue`.

The object class `Message` is just the same as in [this example](https://github.com/YuKitAs/tech-note/blob/master/programming-language/java/concurrency/producer-consumer-problem-with-array-blocking-queue.md).

The producer will create messages and insert them to the queue while the queue is not full, here we add an extra `size` variable because our queue is not bounded:

```java
public class Producer implements Runnable {
    private final Queue<Message> msgQueue;
    private int size;

    public Producer(Queue<Message> msgQueue, int size) {
        this.msgQueue = msgQueue;
        this.size = size;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            Message msg = new Message(Integer.toString(i));

            try {
                Thread.sleep(i);
                produce(msg);
                System.out.println("Produced " + msg.getMsg());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private void produce(Message msg) throws InterruptedException {
        while (msgQueue.size() == size) {
            synchronized (msgQueue) {
                System.out.println("Queue is full. " + Thread.currentThread().getName() + " is waiting.");
                msgQueue.wait();
            }
        }

        synchronized (msgQueue) {
            msgQueue.add(msg);
            msgQueue.notifyAll();
        }
    }
}
```

The consumer will retrieve and remove messages from the queue while the queue is not empty.

```java
public class Consumer implements Runnable {
    private final Queue<Message> msgQueue;

    public Consumer(Queue<Message> msgQueue) {
        this.msgQueue = msgQueue;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Thread.sleep(10);
                System.out.println("Consumed " + consume().getMsg());
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private Message consume() throws InterruptedException {
        while (msgQueue.isEmpty()) {
            synchronized (msgQueue) {
                System.out.println("Queue is empty. " + Thread.currentThread().getName() + " is waiting.");
                msgQueue.wait();
            }
        }

        synchronized (msgQueue) {
            msgQueue.notifyAll();
            return msgQueue.poll();
        }
    }
}
```

The service is used to create a queue that will be shared with `Producer` and `Consumer` threads.

```java
public class ProducerConsumerService {
    public static void main(String[] args) {
        Queue<Message> msgQueue = new LinkedList<>();

        new Thread(new Producer(msgQueue, 5), "Producer").start();
        new Thread(new Consumer(msgQueue), "Consumer").start();
    }
}
```

A possible output:

```
Produced 0
Produced 1
Produced 2
Produced 3
Consumed 0
Produced 4
Produced 5
Consumed 1
Produced 6
Queue is full. Producer is waiting.
Consumed 2
Produced 7
Queue is full. Producer is waiting.
Consumed 3
Produced 8
Queue is full. Producer is waiting.
Consumed 4
Produced 9
Consumed 5
Consumed 6
Consumed 7
Consumed 8
Consumed 9
Queue is empty. Consumer is waiting.
```
