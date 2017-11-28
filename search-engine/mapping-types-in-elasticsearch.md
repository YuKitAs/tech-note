# Mapping Types in Elasticsearch

Before Elasticsearch 6.x, an index can have multiple types. For example, we could use `PUT twitter/_mapping/tweet` and `PUT twitter/_mapping/user` to create two different mappings types `tweet` and `user` for index `twitter`. But now the mapping types are removed, we would see an error message saying "Rejecting mapping update to [twitter] as the final mapping would have more than 1 type: [tweet, user]".

One alternative is to create indices for each document type, eg. a `tweet` index and a `user` index. If we don't want to waste an entire shard for only a few documents, we can also implement custom `type` field as follows:

```text
PUT twitter
{
  "mappings": {
    "doc": {
      "properties": {
        "type": { "type": "keyword" }, 
        "name": { "type": "text" },
        "user_name": { "type": "keyword" },
        "email": { "type": "keyword" },
        "content": { "type": "text" },
        "tweeted_at": { "type": "date" }
      }
    }
  }
}

PUT twitter/doc/user-1
{
  "type": "user", 
  "name": "John Doe",
  "user_name": "john_doe",
  "email": "john.doe@kimchy.com"
}

PUT twitter/doc/tweet-1
{
  "type": "tweet", 
  "user_name": "john_doe",
  "tweeted_at": "2017-11-28",
  "content": "Ich bin wieder da."
}
```

More reference: [Removal of mapping types](https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html), elastic.