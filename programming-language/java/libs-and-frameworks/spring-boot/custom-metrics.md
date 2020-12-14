# Custom Metrics

Spring Boot 2.0 has integrated [Micrometer](https://micrometer.io/) into Spring Boot Actuator to collect metrics, together with Prometheus which stores metric data, we can define and integrate custom metrics to various monitoring systems like Grafana.

Maven dependencies:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-core</artifactId>
</dependency>
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

There are different ways to build a meter like `Counter`:

```java
private final MeterRegistry meterRegistry;
private final Counter counter;

@Autowired
public TestService(MeterRegistry meterRegistry) {
    this.meterRegistry = meterRegistry;
    counter = Counter.builder("requests").register(meterRegistry);
}

public void test() {
    counter.increment();
}
```

With tags (label):

```java
Counter.builder("requests").tag("method", "GET").register(meterRegistry).increment();
```

```java
meterRegistry.counter("requests", "method", "GET").increment();
```

Without injecting `MeterRegistry`:

```java
Metrics.counter("requests", "method", "GET").increment();
```

An example of `Timer` usage:

```java
Timer timer = Timer.builder("request_process").register(meterRegistry);
Timer.Sample sample = Timer.start(meterRegistry);
// do something
sample.stop(timer);
```

Once exposed `metrics` and `prometheus` management endpoints with

```
management.endpoints.web.exposure.include=metrics,prometheus
```

All the metrics names will be listed via `/actuator/metrics`. All the metrics can be viewed via `/actuator/prometheus` including the custom ones (see metrics format in [note](https://github.com/YuKitAs/tech-note/blob/master/monitoring/prometheus-metrics.md)):

```
# HELP request_process_seconds_max  
# TYPE request_process_seconds_max gauge
request_process_seconds_max 0.0
# HELP request_process_seconds  
# TYPE request_process_seconds summary
request_process_seconds_count 0.0
test_timer_seconds_sum 0.0
# HELP requests_total  
# TYPE requests_total counter
requests_total 0.0
```

An example for testing meters defined as private fields like:

```java
private final Counter requestCounter = Metrics.counter("requests");
```

In the test class, we could mock a counter variable and set the original field with reflection:

```java
@Mock
private Counter counter;

@Before
public void setUp() throws NoSuchFieldException {
    FieldSetter.setField(testService, testService.getClass().getDeclaredField("requestCounter"), counter);
}
```

Verify invocation of the counter:

```java
Mockito.verify(counter, times(1)).increment();
```
