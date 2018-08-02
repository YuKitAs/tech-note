# Weak Reference in Java


A weak reference is reference that is not strong enough to protect the referenced object from garbage collection. A typical use-case described by Wikipedia:

> When one has an object where other objects are registered, such as in the observer pattern (particularly in event handling), if a strong reference is kept, objects must be explicitly unregistered, otherwise a memory leak occurs (the lapsed listener problem), while a weak reference removes the need to unregister.

In Java, `java.lang.ref.WeakReference` is used to create a weak reference to an object and the referenced object can be accessed by `get()`.
