# Parallel Stream in Custom Thread Pool

By default, the parallel streams will use the common pool (`ForkJoinPool.commonPool()`), which normally reduces resource usage. A separate custom thread pool can be constructed with a given parallelism level, by default it's equal to the number of available processors.

```java
ForkJoinPool pool = new ForkJoinPool(4);

// submit the parallel stream execution which returns a ForkJoinTask (a Future)
List<Integer> odds = pool.submit(
        () -> IntStream.range(1, 100).parallel().filter(i -> i % 2 == 1).boxed().collect(Collectors.toList())
      ).get();
System.out.println(odds);
```
