Java Cloning

The [`clone()`](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--) method in `java.lang.Object` can create and return a copy of the object. Unlike using the assignment operator, the cloned object will have a new address, so `x.clone() != x` and `x.clone().getClass() == x.getClass()`, which shows the general intent of "copying an object". It's also typical that `x.clone().equals(x)` will be true, but none of these is an absolute requirement for implementing `clone()`.

Basically, the object that needs to be cloned should implement the marker interface `Cloneable` and implement `clone()` by itself (no need to override) with `super.clone()` being invoked first and a `CloneNotSupportedException` being thrown or caught to throw another custom exception:

```java
public class MyObject implements Cloneable {
    /* omitted for simplicity */

    public MyObject clone() throws CloneNotSupportedException {
        return (MyObject) super.clone();
    }
}
```


However, remember that Java cloning is just making shallow copy: if the object contains other objects, only the references to those objects will be copied.

For example, when `MyObject` has a mutable list member, then if the elements in the list of the original object have been changed, the list of the cloned object will also be modified, and vice versa, since they are referring to the same list.

To avoid such cases, we need to implement a deep clone like:

```java
public MyObject clone() throws CloneNotSupportedException {
    MyObject clonedObj = (MyObject) super.clone();
    clonedObj.setOtherObject((OtherObject) clonedObj.getOtherObject().clone());
    return clonedObj;
}
```

If the `CloneNotSupportedException` is actually not expected to be thrown when calling `myObj.clone()`, it's better to check if the class has implemented `Cloneable`:

```java
if (myObj instanceof Cloneable) {
    clonedObj = myObj.clone();
}
```
