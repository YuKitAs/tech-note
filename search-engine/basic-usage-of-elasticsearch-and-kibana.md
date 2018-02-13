# Basic Usage of Elasticsearch and Kibana

Elasticsearch: built over [Lucene](https://lucene.apache.org/core/) and provides a JSON based REST API to refer to Lucene features, and provides a distributed system on top of Lucene.

This tutorial shows how to work with Elasticsearch 6.2, may not be valid for lower versions.

1. Download and install [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) and [Kibana](https://www.elastic.co/jp/downloads/kibana)

2. In Kibana, open `Dev Tools > Console` to use Kibana's Console UI

3. The following are basic commands used in Kibana. They can also be used with `curl`. At the top-right corner of Kibana's console there is an option `Copy as cURL`.

  * List all indices

    ```console
    GET _cat/indices
    ```

    Append `?v` to show headers.

  * Create a new index

    ```console
    PUT <index-name>
    ```

  * Index a document with an ID

    ```console
    PUT <index-name>/<doc-name>/<ID>
    {
      "_comment": "request body should not be empty"
    }
    ```

    If an ID is not explicit specified, use `POST` instead of `PUT` here. Elasticsearch will generate a random ID to index the document.

  * List an index or a document

    ```console
    GET <indexname>
    GET <index-name>/<doc-name>/<ID>
    ```

    Append `?pretty` to return pretty formatted JSON.

  * List all documents of an index

    ```console
    GET <indexname>/_search
    ```

  * Delete an index or a document

    ```console
    DELETE <indexname>
    DELETE <index-name>/<doc-name>/<ID>
    ```

  * Replace an indexed document (i.e. reindex)

    ```console
    PUT <index-name>/<doc-name>/<ID>
    {
      "_comment": "some updated information"
    }
    ```

  * Update an indexed document

    ```console
    POST <index-name>/<doc-name>/<ID>/_update
    {
      "_comment": "some other updated information"
    }
    ```

    What Elasticsearch will do here is delete the old doc and index a new one.

  * Add new mappings to an existing index
    
    ```console
    PUT <index-name>/_mapping/<doc-name>
    {
      "properties": {
        "some_new_mapping_field": {
          "type": "some_mapping_type"
        }
      }
    }
    ```

4. Configuration:

  To enable CORS, add the following lines in `config/elasticsearch.yml`:

  ```yml
  http.cors.allow-origin: "*"
  http.cors.enabled: true

  node.master: true
  ```
