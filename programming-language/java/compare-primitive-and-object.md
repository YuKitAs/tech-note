# Compare Primitive and Object

It's not a good idea to directly use `==` to compare primitive and object like `int a` and `Integer b`, even if it's compilable without explicitly unboxing `a == b.intValue()`. The main concern in this case is, when `b` happens to be null, checking `a == b` will cause NullPointerException. And a primitive cannot be null, as `a == null` will lead to compilation error.

To avoid this, either check `b` is non-null before, or use `Objects.equals(a, b)` which will box the primitive to an object.
