# Reference Types in Java

There are 4 kinds of reference types in Java, the difference lies in the garbage collection mechanism.

## Strong Reference

A strong reference is the default type of reference:

```java
MyClass obj = new MyClass();
```

The object with an active strong reference will not be garbage collected, unless it is explicitly nullified:

```java
obj = null;
```

## Soft Reference

A soft reference is used to create a reference to an exiting object that is already referred to by a strong reference:

```java
MyClass obj = new MyClass();
SoftReference<MyClass> objSoftRef = new SoftReference<>(obj);

obj = null;
System.gc();
System.out.println(objSoftRef.get()); // probably not null
```

The object with a soft reference will be optionally garbage collected before `OutOfMemoryError` is thrown.

## Weak Reference

A weak reference is reference that is not strong enough to protect the referenced object from garbage collection. It's used in `WeakHashMap` to reference the entry objects. Use-case: establishing a DBConnection which is supposed to be garbage collected when the connection is closed.

```java
MyClass obj = new MyClass();
WeakReference<MyClass> objWeakRef = new WeakReference<>(obj);

obj = null;
System.gc();
System.out.println(objWeakRef.get()); // null
```

## Phantom Reference

An object with a phantom reference will not be automatically garbage collected, as it will be enqueued after the garbage collector determines that it's about to be collected.

```java
MyClass obj = new MyClass();
ReferenceQueue<MyClass> refQueue = new ReferenceQueue<>();
PhantomReference<MyClass> objPhantomRef = new PhantomReference<>(obj, refQueue);

System.out.println(objPhantomRef.get()); // always null
System.out.println(objPhantomRef.isEnqueued()); // false

obj = null;
System.gc();
Thread.sleep(1_000);
System.out.println(objPhantomRef.isEnqueued()); // true
```
