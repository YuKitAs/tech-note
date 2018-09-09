# Common Standard Exceptions

The most commonly reused standard exceptions:

| Exception | Occasion for Use |
| --------- | --------- |
| `IllegalArgumentException` | Non-null parameter value is inappropriate for the method to use |
| `IllegalStateException` | Object state is inappropriate for method invocation (eg. Object has not been properly initialized) |
| `NullPointerException` | Parameter value is null where prohibited |
| `IndexOutOfBoundsException` | Index parameter value is out of range |
| `ConcurrentModificationException` | Concurrent modification of an object designed for single-thread has been detected where prohibited |
| `UnsupportedOperationException` | Object does not support method (eg. `Arrays.asList()` returns a fixed-size list which cannot be modified) |
