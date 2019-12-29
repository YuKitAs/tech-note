# Error Handling with Dead-Letter Queue

By default, failed messages will be immediately requeued to the original queue over and over again, which could cause an infinite loop. To avoid the default requeuing, there are two options:

* Configure the property in `application.properties`:
  ```
  spring.rabbitmq.listener.simple.default-requeue-rejected=false
  ```

* Throw an `AmqpRejectAndDontRequeueException`.

To hold undelivered or failed messages we can declare a Dead-Letter Queue (DLQ). The messages in DLQ can be monitored, recovered or reprocessed in a custom way. Spring AMQP doesn't provide a standard mechanism for dead-lettering.

Normally, the original queue should be declared with arguments `x-dead-letter-exchange` which can be empty to indicate the default exchange and `x-dead-letter-routing-key` which is the name of the DLQ.

## Scheduled Messaging with [RabbitMQ Delayed Message Plugin](https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/)

**Use case**: add delay before each new attempt, route expired messages to DLQ.

**Concept**: declare a delayed exchange (`setDelayed(true)`) and bind it to the original queue. Publish failed messages to the delayed exchange with `x-delay` header and [message TTL](https://www.rabbitmq.com/ttl.html#per-message-ttl). The messages will be delivered to the original queue after `x-delay` milliseconds, and dead lettered after expiration.

**Example**: [spring-boot-rabbitmq demo](https://github.com/YuKitAs/spring-boot-rabbitmq/tree/master/src/main/java/yukitas/rabbit/tut6)

## Scheduled Messaging without RabbitMQ Delayed Message Plugin

**Use case**: same as above

**Concept**: instead of declaring the delayed exchange and setting `x-delay` on message, use a delayed queue which uses the original queue as DLQ. Publish failed messages with TTL to a default exchange which will directly route them to the delayed queue, the expired messages in the delayed queue will be routed to the original queue. Check the message TTL *manually* to determine if the message should be handled. The rejected messages will be dead lettered.

**Example**:

Configuration:
```java
@Configuration
@EnableRabbit
public class RabbitConfig {
    @Bean
    public RabbitTemplate delayedTemplate(ConnectionFactory connectionFactory) {
        RabbitTemplate template = new RabbitTemplate(connectionFactory);
        template.setExchange("");
        template.setRoutingKey("original-queue");
        return template;
    }

    @Bean
    public Queue deadLetterQueue() {
        return new Queue("dead-letter-queue");
    }

    @Bean
    public Queue originalQueue() {
        Map<String, Object> args = new HashMap<>();
        args.put("x-dead-letter-exchange", "");
        args.put("x-dead-letter-routing-key", "dead-letter-queue");
        return new Queue("original-queue", true, false, false, args);
    }

    @Bean
    public Queue delayedQueue() {
        Map<String, Object> args = new HashMap<>();
        args.put("x-dead-letter-exchange", "");
        args.put("x-dead-letter-routing-key", "original-queue");
        return new Queue("delayed-queue", true, false, false, args);
    }
}
```

Consumer:
```java
@Autowired
private RabbitTemplate delayedTemplate;

@RabbitListener(queues = "original-queue")
public void handleEvent(Event event, Message message) {
    try {
        // do something
    } catch (Throwable t) {
        if (isExpired(message)) {
            throw new AmqpRejectAndDontRequeueException("Rejected expired message");
        }
        publishToDelayed(event, message);
    }
}

private boolean isExpired(Message message) {
    Date deliveryDate = message.getMessageProperties().getTimestamp();
    return deliveryDate != null && (new Date().getTime() - deliveryDate.getTime()) > 3600000;
}

private void publishToDelayed(Event event, Message msg) {
    MessageProperties props = new MessageProperties();
    props.setContentType(msg.getMessageProperties().getContentType());
    props.setContentEncoding(msg.getMessageProperties().getContentEncoding());
    props.setType(msg.getMessageProperties().getType());
    props.setExpiration(String.valueOf(600000));

    if (msg.getMessageProperties().getTimestamp() != null) {
        props.setTimestamp(msg.getMessageProperties().getTimestamp());
    } else {
        props.setTimestamp(new Date());
    }

    delayedTemplate.send(new Message(msg.getBody(), props));
}
```

## Message Recovering
