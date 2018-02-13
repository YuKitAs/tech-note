# Learning Kibana

## Index Patterns

In order to use Kibana, at least one index pattern should be configured. An index pattern is a string with optional wildcards that match multiple indices, for example `index_*`.

## Discover

After configured an index pattern, we can find all the data of the current set of indices. [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) can be used to search data. By default, all fields are shown for each matching document. We can select and visualize available fields from the left side.
