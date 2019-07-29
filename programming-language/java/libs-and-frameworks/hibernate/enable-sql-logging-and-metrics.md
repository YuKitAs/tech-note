# Enable SQL Logging and Metrics

In `application.properties`, consider to add the following properties.

* Log SQL statements without actual parameters (from `log4j2`):

  ```
  logging.level.org.hibernate.SQL=DEBUG
  ```

  These logs would be useful to understand what are actually executed.

* Log statements with actual parameters (from `log4j2`):

  ```
  logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE
  ```

  These logs could easily overwhelm the console, so they'd better only be logged on a low level.

* Show session metrics (from `spring-data-jpa`):

  ```
  spring.jpa.properties.hibernate.generate_statistics=true
  ```

  The metrics look like:

  ```
  Session Metrics {
    334657 nanoseconds spent acquiring 1 JDBC connections;
    0 nanoseconds spent releasing 0 JDBC connections;
    4830679 nanoseconds spent preparing 7 JDBC statements;
    3717709 nanoseconds spent executing 7 JDBC statements;
    0 nanoseconds spent executing 0 JDBC batches;
    0 nanoseconds spent performing 0 L2C puts;
    0 nanoseconds spent performing 0 L2C hits;
    0 nanoseconds spent performing 0 L2C misses;
    12767381 nanoseconds spent executing 2 flushes (flushing a total of 8 entities and 2 collections);
    7671805 nanoseconds spent executing 2 partial-flushes (flushing a total of 4 entities and 4 collections)
  }
  ```
