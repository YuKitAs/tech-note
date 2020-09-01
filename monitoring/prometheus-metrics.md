# Prometheus Metrics


## Metrics format

A metrics contains:
* metric name
* 0 or multiple lables (key-value arrays)
* current metric value
* optional metric timestamp

Example:
```
# HELP <metric_name> <description>
# TYPE <metric_name> <metric_type>
# Comment
http_requests_total{method="post",code="400"} <value> <timestamp>
```

## Metrics types

* Counter: cumulative values, e.g. the number of total requests to an endpoint
* Gauge: instantaneous measurement of a value, e.g. system load
* Histogram: observed values in configurable buckets, e.g. request time
* Summary: configurable quantiles over a sliding time window, e.g. gc duration
