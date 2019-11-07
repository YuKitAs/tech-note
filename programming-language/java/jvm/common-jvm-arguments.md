# Common JVM Arguments

There are three kinds of options: standard options beginning with `-`, non-standard options beginning with `-X` (Java HotSpot VM specific), and developer options beginning with `-XX` (advanced, not stable).

## Heap Memory

Minimal and maximal heap size for JVM:

```console
-Xms256m -Xmx5G
```

## Garbage Collection

Declare a GC implementation:

```console
-XX:+UseSerialGC
-XX:+UseParallelGC
-XX:+UseParallelOldGC
-XX:+USeParNewGC
-XX:+UseG1GC
-XX:+UseConcMarkSweepGC
```

Set the size of the young generation:

```console
-Xmn1m
```

Set the starting/maximal size of the permanent generation:

```console
-XX:PermSize=20m
-XX:MaxPermSize=20m
```

Log GC activity:

```console
-XX:+PrintGC
-XX:+PrintGCDetails
-XX:+PrintGCDateStamps
-XX:+PrintHeapAtGC
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=10
-XX:GCLogFileSize=50M
-Xloggc:/path/to/gc.log
```
