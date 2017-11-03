# Test Private Method and Variable

Suppose we have to access a private method or variable but it's not allowed to change the code (eg. increase the visibility), using reflection is actually the most practical way.

For example, we have a class with a private variable and a private method like this:

```java
public class MyClass() {
    private int num = 42;

    private int myMethod(int i) {
        return num + i;
    }
}
```

Then we could use reflection to invoke the method in the test class:

```java
MyClass myClass = new MyClass();
Method method = MyClass.class.getDeclaredMethod("myMethod", int.class);
method.setAccessible(true);

int out = (Integer) method.invoke(myClass, 1);
```
And get the variable:

```java
Field field = MyClass.class.getDeclaredMethod("num");
field.setAccessible(true);

int num = field.get(myClass);
```
