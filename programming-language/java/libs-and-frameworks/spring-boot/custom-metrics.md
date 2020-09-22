# Custom Metrics


Spring Boot 2.0 has integrated [Micrometer](https://micrometer.io/) into Spring Boot Actuator to collect metrics, together with [Prometheus](https://prometheus.io/) which stores metric data, we can define and integrate custom metrics to various monitoring systems like Grafana.

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

The following is an example for custom metrics with `Counter` and `Timer`:

```java
@Service
public class TestService {
    private final MeterRegistry meterRegistry;
    private final Counter counter;
    private final Timer timer;

    @Autowired
    public TestService(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        counter = Counter.builder("test_counter").register(meterRegistry);
        timer = Timer.builder("test_timer").register(meterRegistry);
    }

    public void test() {
        counter.increment();

        Timer.Sample sample = Timer.start(meterRegistry);
        // do something
        sample.stop(timer);
    }
}
```

Once exposed `prometheus` management endpoint with `management.endpoints.web.exposure.include=prometheus`, we can call `/actuator/prometheus` to see the metrics (metrics format in [note](https://github.com/YuKitAs/tech-note/blob/master/monitoring/prometheus-metrics.md)):

```
# HELP test_timer_seconds_max  
# TYPE test_timer_seconds_max gauge
# HELP test_timer_seconds  
# TYPE test_timer_seconds summary
# HELP test_counter_total  
# TYPE test_counter_total counter
```
