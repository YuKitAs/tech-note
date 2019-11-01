# JVM Generations

In order to enhance the performance of Garbage Collection, the heap is divided into 3 generations:

## Young Generation

Further divided into Eden Space, Survivor Space 0 (S0) and Survivor Space 1 (S1). The two survivor spaces are needed to avoid memory fragmentation.

When Eden is filled up, it will cause a minor garbage collection to ping-pong live objects from Eden and one of the survivor space to the other, until: 1. when a maximum tenuring threshold (which can be set with `-XX:MaxTenuringThreshold`) is met; 2. there is no more room in survivor space, and then the objects will be moved to the old generation.

Since the events will stop all the threads, they are called "Stop the World" events.

## Old or Tenured Generation

Used to store long surviving objects. Collecting the old generation is called a major garbage collection.

## Permanent Generation

Contains metadata required by the JVM. Unneeded data will be collected in a full garbage collection.
