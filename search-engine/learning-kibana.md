# Learning Kibana

* [Index Patterns](#index-patterns)
* [Discover](#discover)
* [Visualize](#visualize)
* [Dashboard](#dashboard)


## Index Patterns

In order to use Kibana, at least one index pattern should be configured. An index pattern is a string with optional wildcards that match multiple indices, for example `index_*`. Create index pattern in `Management`.

## Discover

After configured an index pattern, we can find all the data of a selected index pattern in `Discover`. Searches can be saved and reloaded with the current search query string and index pattern.

### Query bar

In the query bar, JSON-based [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) or [Lucene query syntax](https://www.elastic.co/guide/en/kibana/current/lucene-query.html) can be used to search data.

The new query language [Kuery](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) which is built for kibana can also be enabled for searching, but it's just an experimental functionality so far by Elasticsearch 6.2.

### Filtering by field values

Besides using search query, there are three ways to add field filters.

1. Expand a document in the document table and click the filter button right to the field name with a certain value.

2. Add from `Available Lields` list. Only top 5 values for each field will be shown. Every field in the `Selected Fields` list will be displayed as a column in the document table.

3. Click `Add a filter`. Either search filter values or build filter by editing Query DSL manually, the latter allows logical query operators.

![](https://www.elastic.co/guide/en/kibana/current/images/PositiveFilter.jpg) Positive Filter button: "filter for this value", equivalent to `is` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/NegativeFilter.jpg) Negative Filter: "filter out this value", equivalent to `is not` operator.

![](https://www.elastic.co/guide/en/kibana/current/images/ExistsButton.jpg) Exists button: "filter for field present".

## Visualize

Fields can be directly visualized from the fields list in `Discover`, or in `Visualize` from a new search.

## Dashboard

Dashboard displays a collection of saved visualizations.
