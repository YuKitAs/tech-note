# JVM Garbage Collectors

## Serial GC

By default in Java SE 5 and 6. Both minor and major garbage collections are done serially using a single virtual CPU and mark-compact collection method.

The mark-compact algorithm: mark reachable objects, a compacting step relocates the marked objects towards the beginning of the heap area.

## Parallel GC

By default on a host with N CPUs, the parallel GC uses N garbage collector threads in the collection. The number of threads can be set with `-XX:ParallelGCThreads=<num_threads>`.

With `-XX+UseParallelGC` we will enable a multi-thread young generation collector with a single-threaded old generation collector, with `-XX:+UseParallelOldGC` the GC is also a multi-thread old generation collector.

The parallel collector is a throughout-oriented collector, it should be used when a lot of work need to be done (application throughout needs to be sped up) and long pauses are acceptable.

## CMS (Concurrent Mark Sweep) GC

Also known as the concurrent low-pause collector, which uses multiple garbage collector threads. Planned to be removed from Java 14 in [JEP 363](https://openjdk.java.net/jeps/363).

## G1 (Garbage-first) GC

Planned to be the new default collector from Java 9 in [JEP-248](https://openjdk.java.net/jeps/248). Parallel, concurrent, incrementally compacting, low-pause. Unlike other GCs, G1 splits the heap into many fix-sized small regions, each region assigned to a space. It doesn't have to collect an entire generation, but regions that are full of garbage. G1 performs better with large heaps, when it has too little heap available, a full GC will be performed. It can be configured to not exceed a maximum pause time by `-XX:MaxGCPauseMillis`.

## ZGC

An experimental GC in Java 11 and in production from Java 15. It uses colored pointers to perform concurrent operations and keep track of heap usage.
