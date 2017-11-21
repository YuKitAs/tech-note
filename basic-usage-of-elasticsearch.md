# Basic Usage of Elasticsearch

1. Download and install [Elasticsearch]( https://www.elastic.co/de/products/elasticsearch ) and [Kibana](https://www.elastic.co/de/products/kibana)

2. In Kibana, open `Dev Tools > Console` to use Kibana's Console UI

3. Basic commands:

* List all indices

```console
GET /_cat/indices?v
```

* Create a new index

```console
PUT /<index-name>?pretty
```

* Index a document with an ID

```console
PUT /<index-name>/<doc-name>/<ID>?pretty
{
  "_comment": "request body should not be empty"
}
```

If an ID is not explicit specified, use `POST` instead of `PUT` here. Elasticsearch will generate a random ID to index the document.

* List an index or a document

```console
GET /<indexname>?pretty
GET /<index-name>/<doc-name>/<ID>?pretty
```

* Delete an index or a document

```console
DELETE /<indexname>?pretty
DELETE /<index-name>/<doc-name>/<ID>?pretty
```

* Replace an indexed document (i.e. reindex)

```console
PUT /<index-name>/<doc-name>/<ID>?pretty
{
  "_comment": "some updated information"
}
```

* Update an indexed document

```console
POST /<index-name>/<doc-name>/<ID>/_update?pretty
{
  "_comment": "some other updated information"
}
```

What Elasticsearch will do here is delete the old doc and index a new one.