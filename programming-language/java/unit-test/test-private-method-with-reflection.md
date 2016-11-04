# Test Private Method With Reflection

Suppose we want to test a private method but it's not allowed to increase the visibility of the method, using reflection is actually the most practical way.

For example, we have a class with a private method like this:

```java
public class MyClass() {        
    private int myMethod(int i) {
        return i + 42;
    }
}
```

Then we could use reflection to get the method in the test class:

```java
MyClass myClass = new MyClass();
Method method = MyClass.class.getDeclaredMethod("myMethod", int.class);
method.setAccessible(true);
```

By `setAccessible(true)` we can now invoke the method and get the returned value:

```java
int out = (Integer) method.invoke(myClass, 0);
```
