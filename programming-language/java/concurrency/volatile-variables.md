# Volatile Variables

`volatile` keyword guarantees the value of the volatile variable will be read from main memory instead of from thread's local cache. It means, threads will automatically see the most up-to-date value for volatile variables.

Volatile variables can be used to provide `thread safety`. A typical example is:

```java
volatile int i = 0;

public void increment(){
   i++;
}
```

More reference: [Managing volatility](https://www.ibm.com/developerworks/java/library/j-jtp06197/index.html). IBM, 2007.
