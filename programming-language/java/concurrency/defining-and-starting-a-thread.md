# Defining and Starting a Thread

There are 2 ways to create and run threads.

### Method 1: Creation by implementing `Runnable` Interface

We create a class that initializes and starts a thread in the constructor. The task of this thread is to print five numbers in sequence, which is defined in the `run()` method.

The `run()` method will be executed after `start()` is called. The `start()` method will return as soon as the thread is started, it won't wait until the `run()` method is finished.

```java
public class MyRunnable implements Runnable {
    Thread thread;

    MyRunnable() {
        thread = new Thread(this, "Runnable child thread");
        System.out.println(thread + " created.");
        thread.start();
    }

    @Override
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

Then we initialize a child thread in the `main()` method so it'll be started and run. `isAlive()` is used to check if the child thread is running.

```java
public class RunnableDemo {
    public static void main(String[] args) {
        MyRunnable myRunnable = new MyRunnable();

        try {
            while (myRunnable.thread.isAlive()) {
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

This time we will create a child thread directly, so we use `start()` in the constructor.

```java
public class MyThread extends Thread {
    MyThread() {
        super("Runnable child thread");
        System.out.println(this + " created.");
        start();
    }

    @Override
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

In the `main()` method, replace `MyRunnable myRunnable = new MyRunnable();` with `MyThread myThread = new MyThread()` and replace `myRunnable.thread.isAlive()` with `myThread.isAlive()`, then we can get the same output as using the first method.

The advantages of the first method are:

1. the object can extend other class than `Thread`, thus more flexible

2. the task could be sent to web, but `Thread` is not serializable
