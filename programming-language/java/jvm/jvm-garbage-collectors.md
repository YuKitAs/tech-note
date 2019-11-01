# JVM Garbage Collectors

## Serial GC

By default in Java SE 5 and 6. Both minor and major garbage collections are done serially using a single virtual CPU and mark-compact collection method.

## Parallel GC

By default on a host with N CPUs,the parallel GC uses N garbage collector threads in the collection. The number of threads can be set with `-XX:ParallelGCThreads=<num_threads>`.

With `-XX+UseParallelGC` we will enable a multi-thread young generation collector with a single-threaded old generation collector, with `-XX:+UseParallelOldGC` the GC is also a multi-thread old generation collector.

The parallel collector should be used when a lot of work need to be done (application throughout needs to be sped up) and long pauses are acceptable.


## CMS (Concurrent Mark Sweep) GC

Also known as the concurrent low pause collector. Planned to be removed in [JEP 363](https://openjdk.java.net/jeps/363).

## G1 (Garbage-first) GC

Planned to replace CMS. Parallel, concurrent, incrementally compacting, low-pause.
