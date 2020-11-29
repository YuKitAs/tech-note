# `CompletableFuture`

Since Java 8, `CompletableFuture` has been introduced for asynchronous computation.

The `get()` method used to retrieve the computation result is blocking, it will wait until the future is done, but `CompletableFuture` can also be manually completed like:

```java
CompletableFuture<String> completableFuture = new CompletableFuture<>();
completableFuture.complete("Hello World");
```

Static methods like `runAsync()` and `supplyAsync()` allow us to create a `CompletableFuture` from `Runnable` and `Supplier` instances and execute the tasks in a separate thread (thread from the common pool will be used by default, an optional thread pool can also be specified). The result can be processed with (a sequence of) `thenApply()`, `thenAccept()` or `thenRun()`, for example:

```java
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> "World")
        .thenApply(name -> "Hello " + name);
System.out.println(completableFuture.get());
```

## Combine futures

`thenCompose()` is used to combine two dependent futures, `thenCombine()` is used to combine two independent futures and do something when both futures are complete.


## Error handling

The `exceptionally()` method can be used to log the exception and return a default value:

```java
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> {
    // do something that would throw exception
    return "Hello World";
}).exceptionally(ex -> {
    System.out.println("Something went wrong: " + ex.getMessage());
    return "Unknown";
});
```
