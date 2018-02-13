# Usage of Suggesters

There are different kinds of [suggesters](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html) to suggest similar terms based on a input text, such as `term` suggester, `phrase` suggester, `completion` suggester and `context` suggester.

The `completion` suggester provides auto-complete feature and is optimized for speed using data structures.

First of all, for an existing index, we must specify a completion suggester for a field, here the `name_suggest` field:

```console
PUT <index-name>/_mapping/<doc-name>
{
    "properties" : {
        "name" : {
            "type": "keyword"
        },
        "name_suggest" : {
            "type" : "completion"
        }
    }
}
```

Then, index documents with field `name_suggest`:

```console
PUT <index-name>/<doc-name>/<ID>
{
  "name" :         "Super cool name",
  "name_suggest" : "Super cool name"
}
```

Now we can query for suggestions. Notice that in Elasticsearch 6.2, `_suggest` endpoint has been deprecated, we should use `_search` instead. Each suggestion should be identified with an arbitrary name, here `my_suggest`. `size` is the number of suggestions to return (default to 5):

```console
POST <index-name>/_search
{
    "suggest": {
        "my_suggest" : {
            "prefix" : "s",
            "completion" : {
                "field" : "name_suggest",
                "size" : 10
            }
        }
    }
}
```

The suggestion response for `my-suggest` will be returend.

More reference:
* [Completion Suggester](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters-completion.html), Elasticsearch Reference [6.2].
