# Learning Kibana

* [Index Patterns](#index-patterns)
* [Discover](#discover)
* [Visualize](#visualize)
* [Dashboard](#dashboard)
* [Timelion](#timelion)
* [Dev Tools](#dev-tools)

## Index Patterns

In order to use Kibana, at least one index pattern should be configured. An index pattern is a string with optional wildcards that match multiple indices, for example `index_*`. Create index pattern in `Management > Index Patterns`.

## Discover

After configured an index pattern, we can find all the data of a selected index pattern in `Discover`. Searches can be saved, reloaded, exported as JSON with the current search query string and index pattern. The saved searches can be managed in `Management > Saved Objects > Searches`.

### Query bar

In the query bar, JSON-based [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) and [Lucene query syntax](https://www.elastic.co/guide/en/kibana/current/lucene-query.html) are supported to search data.

The new query language [Kuery](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) which is built for kibana can also be enabled for searching, but it's just an experimental functionality so far by Elasticsearch 6.2.

A string without double quotation marks would be used to match any documents containing one of the words in the string. For example, the string query `test client` equals to `"test" OR "client"`.

Leave blank for matching all.

### Filtering by field values

Besides using search query, there are three ways to add field filters.

1. Expand a document in the document table and click the filter button right to the field name with a certain value.

2. Add from `Available Fields` list. Only top 5 values for each field will be shown. Every field in the `Selected Fields` list will be displayed as a column in the document table.

3. Click `Add a filter` to either search filter values or build filter by editing Query DSL manually, the latter allows logical query operators.

![](https://www.elastic.co/guide/en/kibana/current/images/PositiveFilter.jpg) **Positive Filter** button: "filter for this value", equivalent to `is` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/NegativeFilter.jpg) **Negative Filter** button: "filter out this value", equivalent to `is not` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/ExistsButton.jpg) **Exists** button: "filter for field present".

## Visualize

Fields can be directly visualized from the fields list in `Discover`, or in `Visualize` from a new search or a saved search. A visualization with link to a saved search can be saved and exported as CSV or JSON. The saved visualizations can be managed in `Management > Saved Objects > Visualizations`.

## Dashboard

A Dashboard displays a collection of saved visualizations. Specific time range can be set for the current dashboard. The saved dashboards can be managed or exported as JSON in `Management > Saved Objects > Dashboards`.

## Timelion

Timelion is a tool for time series analysis from [Metricbeat](https://www.elastic.co/guide/en/beats/metricbeat/current/index.html). We need to define different arguments in `.es()`, such as `index`, `timefield`, `metric`, `offset` etc. I haven't actually tried out Timelion, please refer to detailed [official docs](https://www.elastic.co/guide/en/kibana/current/timelion-getting-started.html).

## Dev Tools

For basic usage of composing requests in `Dev Tools` see this [note](https://github.com/YuKitAs/tech-note/blob/master/search-engine/basic-usage-of-elasticsearch-and-kibana.md). Multiple requests are supported.