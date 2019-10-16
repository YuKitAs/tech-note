# Common JVM Arguments

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
-XX:+USeParNewGC
-XX:+UseG1GC
```

Log GC activity:

```console
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=10
-XX:GCLogFileSize=50M
-Xloggc:/path/to/gc.log
```
