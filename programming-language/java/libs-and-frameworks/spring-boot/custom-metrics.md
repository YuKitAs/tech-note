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
        Timer.Sample sample = Timer.start(meterRegistry);
        // do something
        counter.increment();
        sample.stop(timer);
    }
}
```

Once exposed `metrics` and `prometheus` management endpoints with `management.endpoints.web.exposure.include=metrics,prometheus`, we can call `/actuator/metrics` to see all the metrics names and  and call `/actuator/prometheus` to see the metrics (metrics format in [note](https://github.com/YuKitAs/tech-note/blob/master/monitoring/prometheus-metrics.md)):

```
# HELP test_timer_seconds_max  
# TYPE test_timer_seconds_max gauge
test_timer_seconds_max 0.0
# HELP test_timer_seconds  
# TYPE test_timer_seconds summary
test_timer_seconds_count 0.0
test_timer_seconds_sum 0.0
# HELP test_counter_total  
# TYPE test_counter_total counter
test_counter_total 0.0
```
