# `Instant` and `LocalDateTime`

Since Java 8, it's recommended to use immutable `Instant` and `LocalDateTime` instead of the mutable `Date` classes.

The main difference between `Instant` and `LocalDateTime` is that `Instant` is calculated independently of time zone. If we print `Instant.now()` and `LocalDateTime.now()` we will notice the time difference immediately.

## Custom Timezone

```java
LocalDateTime.now(ZoneId.of("Asia/Tokyo"));
Instant.now().atZone(ZoneId.of("Asia/Tokyo"));
```

## Formatting with Custom Pattern

```java
LocalDateTime.now().format(DateTimeFormatter.ofPattern("dd MMMM yyyy, HH:mm:ss")));
DateTimeFormatter.ofPattern(("yyyy-mm-dd'T'HH:mm:ss[.SSSSSS]").format(LocalDateTime.now()));
DateTimeFormatter.ofPattern(("yyyy-mm-dd'T'HH:mm:ss[.SSSSSS]").format(Instant.now().atZone(ZoneId.systemDefault())));
```

When formating `Instant`, a timezone is required, otherwise an `UnsupportedTemporalTypeException` will be thrown.

## Conversion

Convert `Instant` to `LocalDateTime`:

```java
LocalDateTime localDateTime = LocalDateTime.ofInstant(Instant.now(), ZoneOffset.UTC);
```

Convert `LocalDateTime` to `Instant`:

```java
Instant instant = LocalDateTime.now().toInstant(ZoneOffset.UTC);
```
