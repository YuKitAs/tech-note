# `CompletableFuture`


Since Java 8, `CompletableFuture` has been introduced for asynchronous computation.

The `get()` method used to retrieve the computation result is blocking, it will wait until the future is done, but `CompletableFuture` can also be manually completed like:

```java
CompletableFuture<String> completableFuture = new CompletableFuture<>();
completableFuture.complete("Hello World");
```

Static methods like `runAsync()` and `supplyAsync()` allow us to create a `CompletableFuture` from `Runnable` and `Supplier` instances, the result can be processed with a sequence of `thenApply()`, `thenAccept()` or `thenRun()`:

```java
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> "World")
        .thenApply(name -> "Hello " + name);
System.out.println(completableFuture.get());
```

To process the result in another thread than where the `supplyAsync()` task is executed, we can use `thenApplyAsync()` (thread from the common pool will be used by default, an optional thread pool can also be specified):

```java
Executor executor = Executors.newFixedThreadPool(2);
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> "World")
        .thenApplyAsync(name -> "Hello " + name, executor);
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

Java 9 introduced support for delays and timeouts.

## Delay

`delayedExecutor` can be used together with the `completeAsync()` method:

```java
CompletableFuture<String> completableFuture = new CompletableFuture<String>().completeAsync(
        () -> "Goodbye World", CompletableFuture.delayedExecutor(3, TimeUnit.SECONDS));
```

## Timeout handling

Return a default value after a specific timeout:

```java
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> {
    // do something that would cause timeout
    return "Hello World";
}).completeOnTimeout("Goodbye World", 1, TimeUnit.MINUTES);
```

Throw `TimeoutException`:

```java
CompletableFuture<String> completableFuture = CompletableFuture.supplyAsync(() -> {
    // do something that would cause timeout
    return "Hello World";
}).orTimeout(1, TimeUnit.MINUTES);
```
