# Parallel Stream in Custom Thread Pool


```java
ForkJoinPool pool = new ForkJoinPool(4);
List<Integer> odds = pool.submit(
        () -> IntStream.range(1, 100).parallel().filter(i -> i % 2 == 1).boxed().collect(Collectors.toList()))
        .get();
System.out.println(odds);
pool.shutdown();
```
