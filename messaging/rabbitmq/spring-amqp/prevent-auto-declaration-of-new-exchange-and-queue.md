# Prevent Auto Declaration of New Exchange and Queue

When an exchange or queue already exists and we don't want the AmqpAdmin to declare new ones, we can manually set the `shouldDeclare` parameter in an exchange or queue `Bean` like:

```java
@Bean
public FanoutExchange exchange() {
    FanoutExchange exchange = new FanoutExchange(EXCHANGE_NAME);
    exchange.setShouldDeclare(false); // default is true

    return exchange;
}

@Bean
public Queue queue() {
    Queue queue = new Queue(QUEUE_NAME);
    queue.setShouldDeclare(false); // default is true

    return queue;
}
```
