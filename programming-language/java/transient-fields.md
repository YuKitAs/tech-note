# Transient Fields

Variables marked `transient` are not part of the persistent state of an object and won't be serialized. Use-cases: sensitive data, derivable/computable data.

It has no impact if used together with `static` or `final`:

```java
public class Test implements Serializable {
    private int i = 42;
    private transient int j = 43;
    private transient static int a = 2;
    private transient final int b = 3;

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Test test = new Test();

        // serialization
        ObjectOutputStream oo = new ObjectOutputStream(new FileOutputStream("test.txt"));
        oo.writeObject(test);

        // deserialization
        ObjectInputStream oi = new ObjectInputStream(new FileInputStream("test.txt"));
        Test output = (Test) oi.readObject();
        System.out.println("i = " + output.i);
        System.out.println("j = " + output.j);
        System.out.println("a = " + output.a);
        System.out.println("b = " + output.b);
    }
}
```

Output:
```
i = 42
j = 0
a = 2
b = 3
```
