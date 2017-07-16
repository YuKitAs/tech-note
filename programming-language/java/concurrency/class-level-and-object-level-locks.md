# Class Level and Object Level Locks

In java there are two types of locks (see examples below).

Class level lock assures that only one thread will be able to execute `method1()` in any one of the `Demo` instance at a time, all the other instances will be locked. It's used to make static data thread safe.

Object level lock assures that only one thread will be able to execute `method2()` of a given `Demo` instance. It's used to make instance level thread safe.

```java
public class Demo {
    // class level lock
    public synchronized static void method1() {}

    // object level lock
    public synchronized void method2() {}
}
```
Or

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

`method1()` and `method2()` can be run concurrently.
