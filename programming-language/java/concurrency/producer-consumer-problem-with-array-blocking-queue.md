# Producer-Consumer Problem With ArrayBlockingQueue

Here is an example for the implementation of Producer-Consumer Problem using java ArrayBlockingQueue. The two most important methods for BlockingQueue are `put()` and `take()`.

`put(E e)` is used to insert an element to the queue. If the queue is full, it will wait until there is space available.

`E take()` is to retrieve the element from the head of the queue. If the queue is empty, it will wait until there is an element available.

The object class is defined as follows:

```java
public class Message {
    private String msg;

    public Message(String msg) {
        this.msg = msg;
    }

    public String getMsg() {
        return msg;
    }
}
```

The producer will create messages and put them in the queue.

```java
public class Producer implements Runnable {
    private BlockingQueue<Message> msgQueue;

    public Producer(BlockingQueue<Message> msgQueue) {
        this.msgQueue = msgQueue;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            Message msg = new Message(Integer.toString(i));

            try {
                Thread.sleep(i);
                msgQueue.put(msg);
                System.out.println("Produced " + msg.getMsg());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        Message msg = new Message("exit");

        try {
            msgQueue.put(msg);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

The consumer will take messages from the queue and terminate when it receives the exit message.

```java
public class Consumer implements Runnable {
    private BlockingQueue<Message> msgQueue;

    public Consumer(BlockingQueue<Message> msgQueue) {
        this.msgQueue = msgQueue;
    }

    @Override
    public void run() {
        try {
            Message msg;
            while (!(msg = msgQueue.take()).getMsg().equals("exit")) {
                Thread.sleep(10);
                System.out.println("Consumed " + msg.getMsg());
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

The service is used to create an ArrayBlockingQueue with fixed size, which will be shared with producer and consumer threads.

```java
public class ProducerConsumerService {
    public static void main(String[] args) {
        BlockingQueue<Message> queue = new ArrayBlockingQueue<Message>(10);

        Producer producer = new Producer(queue);
        Consumer consumer = new Consumer(queue);

        new Thread(producer).start();
        new Thread(consumer).start();

        System.out.println("Producer and Consumer have been started.");
    }
}
```

A possible output:

```
Producer and Consumer have been started.
Produced 0
Produced 1
Produced 2
Produced 3
Consumed 0
Produced 4
Produced 5
Consumed 1
Produced 6
Produced 7
Consumed 2
Produced 8
Consumed 3
Produced 9
Consumed 4
Consumed 5
Consumed 6
Consumed 7
Consumed 8
Consumed 9
```
