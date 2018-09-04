# `Instant` and `LocalDateTime`

Since Java 8, it's recommended to use immutable `Instant` and `LocalDateTime` instead of the mutable `Date` classes.

The main difference between `Instant` and `LocalDateTime` is that `Instant` is calculated independently of time zone. If we print `Instant.now()` and `LocalDateTime.now()` we will notice the time difference immediately.

We can choose a time zone for `LocalDateTime` like:

```java
LocalDateTime.now(ZoneId.of("Asia/Tokyo"));
```

It can be easily formatted with a custom pattern like:

```java
LocalDateTime.now().format(DateTimeFormatter.ofPattern("dd MMMM yyyy, HH:mm:ss")));
```

Convert `Instant` to `LocalDateTime`:

```java
LocalDateTime localDateTime = LocalDateTime.ofInstant(Instant.now(), ZoneOffset.UTC);
```

Convert `LocalDateTime` to `Instant`:

```java
Instant instant = LocalDateTime.now().toInstant(ZoneOffset.UTC);
```
