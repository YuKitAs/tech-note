# Multithreading Implementation

There are 2 ways to create threads.

### Method 1: Creation by implementing `Runnable` Interface

We create a class that initializes and starts a thread in the constructor. The task of this thread is to print five numbers in sequence, which is defined in the `run()` method.

```java
public class MultithreadingDemo implements Runnable {
    Thread thread;

    MultithreadingDemo() {
        thread = new Thread(this, "Runnable child thread");
        System.out.println(thread + " created.");
        thread.start();
    }

    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("Count: " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Child thread is interrupted");
        }

        System.out.println("Child thread is finished.");
    }
}
```

Then we initialize a child thread in the `main()` method and make it run. `isAlive()` is used to check if the child thread is running.

```java
public class RunnableDemo {
    public static void main(String[] args) {
        MultithreadingDemo multithreading = new MultithreadingDemo();

        try {
            while (multithreading.thread.isAlive()) {
                System.out.println("Main thread is alive.");
                Thread.sleep(1500);
            }
        } catch (InterruptedException e) {
            System.out.println("Main thread is interrupted.");
        }

        System.out.println("Main thread is finished.");
    }
}
```

Here is the output that we get:

```
Thread[Runnable child thread,5,main] created.
Main thread is alive.
Count: 0
Count: 1
Main thread is alive.
Count: 2
Main thread is alive.
Count: 3
Count: 4
Main thread is alive.
Child thread is finished.
Main thread is finished.
```

### Method 2: Creation by extending `Thread` Class

This time we will create a child thread directly, so we use `start()` directly in the constructor.

```java
public class MultithreadingDemo extends Thread {
    MultithreadingDemo() {
        super("Runnable child thread");
        System.out.println(this + "created.");
        start();
    }

    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("Count: " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Child thread is interrupted");
        }

        System.out.println("Child thread is finished.");
    }
}
```

In the `main()` method, replace `multithreading.thread.isAlive()` with `multithreading.isAlive()` and then we can get the same output as using the first method.
