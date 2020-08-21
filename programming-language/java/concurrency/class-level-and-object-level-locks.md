# Class Level and Object Level Locks

In Java, when using a synchronized block, monitors (intrinsic locks) are used internally to provide synchronization on an object, as all the methods of a monitor will be executed with mutual exclusion.

There are two types of locks:

Class level lock assures that only one thread will be able to execute `method1()` in any one of the `Demo` instance at a time, all the other instances will be locked. It's used to make static data thread safe.

Object level lock assures that only one thread will be able to execute `method2()` of a given `Demo` instance. It's used to make instance level thread safe.

The following two examples of how to use class level and object level locks are equivalent.

Synchronized methods:

```java
public class Demo {
    // class level lock
    public synchronized static void method1() {}

    // object level lock
    public synchronized void method2() {}
}
```

Synchronized statements (specify the object to synchronize and can avoid invocations of other objects' methods):

```java
public class Demo {
    // class level lock
    public static void method1() {
        synchronized (Demo.class) {}
    }

    // object level lock
    public void method2() {
        synchronized (this) {}
    }
}
```

`method1()` and `method2()` can be executed concurrently.
