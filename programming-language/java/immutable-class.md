# Immutable Class

An immutable class is a class whose instances cannot be modified, thus immutable object are inherently thread-safe. Some popular immutable classes in Java are `String`, the boxed primitive classes (`Integer`, `Boolean`...), `BigInteger` and `BigDecimal`.

To define an immutable class, the following rules should be obeyed:

1. No mutators that can modify the object's state (e.g. avoid setter methods).

2. The class can't be extended (e.g. make it `final` or use private constructor with public static factories).

3. All fields are final.

4. All fields are private.

5. Exclusive access to any mutable objects (e.g. make defensive copies instead of the real instances).

The major disadvantage of immutable classes is the potential performance problem because for each distinct value a new object will be created. Sometimes, in order to achieve satisfactory performance, the public mutable companion class is preferable, e.g. using `StringBuilder` instead of `String` (see [note](https://github.com/YuKitAs/tech-note/blob/master/programming-language/java/string-concatenation.md)).
