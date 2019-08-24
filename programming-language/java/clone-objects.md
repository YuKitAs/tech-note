# Clone Objects

The `clone()` method in `java.lang.Object` can create and return a copy of the object, and it is protected.

The object that needs to be cloned should implement the marker interface `Cloneable` and implement `clone()` by itself (no need to override) with the `super.clone()` invoked first:

```java
public class MyObject implements Cloneable {
    /* omitted for simplicity */

    public MyObject clone() throws CloneNotSupportedException {
        return (MyObject) super.clone();
    }
}
```

Unlike using the assignment operator, the cloned object is not the original object, that means `myObj.clone() != myObj`.

However, when the object contains other objects, only the references will be copied. For example, when `MyObject` has `List<String> attr`, then the cloned object will only get the address to this list. Thus if the elements of the mutable list of the original `myObj` have changed, calling `getAttr()` of the cloned object will also return the modified list.
