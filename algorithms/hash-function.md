# Hash Function

Hashing is a method to reference key-value pairs more efficiently by transforming search keys into array indices with arithmetic operations - hash functions.

A good hash function must meet the following primary requirements:

* Deterministic - equal keys must produce the same hash value
* Efficient to compute
* Uniformly distribute the keys

In Java, every data type must implement `hashCode()` method which returns a 32-bit integer and it should always be consistent with `equals()`, so that if two objects are equal they must have the same hash code. If unequal, producing distinct hash codes will improve the performance of hash tables, though not required. The worst but legal implementation of `hashCode()` is always returning a constant integer.

For example, the hash code for a String object in Java is computed as:

```java
public int hashCode() {
    int h = hash; // Default to 0
    if (h == 0 && value.length > 0) {
        char val[] = value;

        for (int i = 0; i < value.length; i++) {
            h = 31 * h + val[i];
        }
        hash = h;
    }
    return h;
```

This is a most traditional implementation of hash function. 31 was chosen because it's an odd prime and the multiplication can be optimized into shift + subtraction for better performance: `31 * i == (i << 5) - i`. A greater prime is even better and leads to much less collisions.
