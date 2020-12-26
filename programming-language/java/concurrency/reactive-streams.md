# Reactive Streams

[Reactive streams](http://www.reactive-streams.org/) is a standard for asynchronous stream processing with non-blocking backpressure.

Java 9 introduced the [Flow API](https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/Flow.html) which corresponds to the Reactive Streams specification. It provides 4 interfaces: `Processor<T, R>`, `Publisher<T>`, `Subscriber<T>` and `Subscription`. Messages produced by a Publisher will be consumed by one or more Subscribers. A message is managed by a Subscription.

Example of use:

Message:

```java
public class Image {
    private int length;
    private int width;

    // constructor, getters and setters

    @Override
    public String toString() {
        return String.format("Image[%dx%d]", length, width);
    }
}
```

Publisher:

```java
public class ImageServer extends SubmissionPublisher<Image> {
    public ImageServer() {
        super(Executors.newSingleThreadExecutor(), 3);
    }
}
```

Subscriber:

```java
public class ImageViewer implements Flow.Subscriber<Image> {
    Flow.Subscription subscription;

    @Override
    public void onSubscribe(Flow.Subscription subscription) {
        this.subscription = subscription;
        subscription.request(1);
    }

    @Override
    public void onNext(Image item) {
        System.out.println("Read image: " + item);
        subscription.request(1);
    }

    @Override
    public void onError(Throwable throwable) {
        throwable.printStackTrace();
    }

    @Override
    public void onComplete() {
        System.out.println("Image read");
    }
}
```

Use `offer()` to let the Publisher provide random items for the Subscriber to subscribe on.

```java
ImageServer imageServer = new ImageServer();
imageServer.subscribe(new ImageViewer());

ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
executor.scheduleWithFixedDelay(() -> imageServer.offer(new Image(new Random().nextInt(100) + 1,
        new Random().nextInt(100) + 1), (sub, item) -> {
    sub.onError(new RuntimeException("Image dropped because of backpressure"));
    return true;
}), 0, 1, TimeUnit.SECONDS);
```

The example above can also be implemented with `Flowable` of RxJava.

A Processor is both Publisher and Subscriber that transforms messages and submits them to the next Subscriber.

Example:

```java
public class TransformProcessor<Image> extends SubmissionPublisher<Image> implements Flow.Processor<Image, Image> {
    private final Function<Image, Image> function;
    private Flow.Subscription subscription;

    public TransformProcessor(Function<Image, Image> function) {
        super();
        this.function = function;
    }

    @Override
    public void onSubscribe(Flow.Subscription subscription) {
        this.subscription = subscription;
        subscription.request(1);
    }

    @Override
    public void onNext(Image item) {
        submit(function.apply(item));
        subscription.request(1);
    }

    @Override
    public void onError(Throwable throwable) {
        throwable.printStackTrace();
    }

    @Override
    public void onComplete() {
        System.out.println("Image transformed");
    }
}
```

```java
ImageServer imageServer = new ImageServer();
TransformProcessor<Image> processor = new TransformProcessor<>(image -> {
    image.setLength(image.getLength() / 2);
    image.setWidth(image.getWidth() / 2);
    return image;
});
imageServer.subscribe(processor);
processor.subscribe(new ImageViewer());

ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
executor.scheduleWithFixedDelay(() -> imageServer.offer(new Image(new Random().nextInt(100) + 1,
        new Random().nextInt(100) + 1), (sub, item) -> {
    sub.onError(new RuntimeException("Image dropped because of backpressure"));
    return true;
}), 0, 1, TimeUnit.SECONDS);
```
