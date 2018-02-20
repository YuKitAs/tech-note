# Learning Kibana

* [Index Patterns](#index-patterns)
* [Discover](#discover)
* [Visualize](#visualize)
* [Dashboard](#dashboard)
* [Timelion](#timelion)
* [Dev Tools](#dev-tools)

Current version: 6.2.1

## Index Patterns

In order to use Kibana, at least one index pattern should be configured. An index pattern is a string with optional wildcards that match multiple indices, for example `index_*`. Create index pattern in `Management > Index Patterns`.

## Discover

After configured an index pattern, we can find all the data of a selected index pattern in `Discover`. Searches can be saved, reloaded, exported as JSON with the current search query string and index pattern. The saved searches can be managed in `Management > Saved Objects > Searches`.

### Query bar

In the query bar, JSON-based [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) and [Lucene query syntax](https://www.elastic.co/guide/en/kibana/current/lucene-query.html) are supported to search data. For example, we can search with `DB: 132 OR DB: 085 OR DB: 062`.

The new query language [Kuery](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) which is built for kibana can also be enabled for searching, but it's just an experimental functionality so far.

A string without double quotation marks would be used to match any documents containing one of the words in the string. For example, the string query `test client` equals to `"test" OR "client"`.

Leave blank for matching all.

### Selected fields

In the lists on the left side, top 5 values for each field will be shown. Every field added from `Available Fields` to `Selected Fields` will be displayed as a column in the document table.

![](https://github.com/YuKitAs/tech-note/blob/master/search-engine/screenshots/kibana-field-list.PNG)

### Filtering by field values

Besides using search query, there are three ways to add field filters.

1. Expand a document in the document table and click the filter button right to the field names.

2. Add from `Available Fields` or `Selected Fields` list by clicking the filter button.

3. Click `Add a filter` to choose a field, an operator and a value, or more advanced, build filter by editing Query DSL manually, this way allows us to use logical query operators, for example

```json
{
  "query": {
    "query_string": {
      "default_field": "*",
      "query": "DB: 132 OR DB: 085 OR DB: 062",
      "analyze_wildcard": true
    }
  }
}
```

Filter buttons mentioned above:

![](https://www.elastic.co/guide/en/kibana/current/images/PositiveFilter.jpg) **Positive Filter** button: "filter for this value", equivalent to `is` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/NegativeFilter.jpg) **Negative Filter** button: "filter out this value", equivalent to `is not` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/ExistsButton.jpg) **Exists** button: "filter for field present".

## Visualize

Fields can be directly visualized from the fields list in `Discover`, or in `Visualize` from a new search or a saved search. A visualization with link to a saved search can be saved and exported as CSV or JSON. The saved visualizations can be managed in `Management > Saved Objects > Visualizations`.

The following is a visualization created from the above saved search:

![](https://github.com/YuKitAs/tech-note/blob/master/search-engine/screenshots/kibana-visualization-example.PNG)

_Y-Axis: Count, X-Axis: DB, Split Series: GROUP_


## Dashboard

A Dashboard displays a collection of saved visualizations. Specific time range can be set for the current dashboard. The saved dashboards can be managed or exported as JSON in `Management > Saved Objects > Dashboards`.

## Timelion

Timelion is a tool for time series analysis from [Metricbeat](https://www.elastic.co/guide/en/beats/metricbeat/current/index.html). We need to define different arguments in `.es()`, such as `index`, `timefield`, `metric`, `offset` etc. I haven't actually tried out Timelion, please refer to detailed [official docs](https://www.elastic.co/guide/en/kibana/current/timelion-getting-started.html).

## Dev Tools

For basic usage of composing requests in `Dev Tools` see this [note](https://github.com/YuKitAs/tech-note/blob/master/search-engine/basic-usage-of-elasticsearch-and-kibana.md). Multiple requests are supported.
