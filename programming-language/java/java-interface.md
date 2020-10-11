# Java Interface

In modern Java, an interface can contain the following members:


1. **Constant variables**

  Fields defined in an interface are public, static and final. However, the constant interface pattern is regarded as a bad practice according to Effective Java.

2. **Abstract methods**

  The methods that need to be implemented.

3. **Default methods** (since Java 8)

  Public methods with default implementations.

4. **Static methods** (since Java 8)

  Public static methods with implementations, mostly are utility methods.

5. **Private methods** (since Java 9)

  For reusing common code in default methods without exposing them publicly.

6. **Private static methods** (since Java 9)

  For reusing common code in static methods without exposing them publicly.
