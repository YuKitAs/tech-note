# `curl` Commands

## Basics

`curl` commands are frequently used to test RESTful web services. One of the most useful commands is:

```console
$ curl -X <method>
```

where method could be `GET`, `POST`, `PUT` or `DELETE`.

Since cURL 7.45.0, it's often unnessary to set `-X` (or `-request`) because the method can be inferred.

Use `-H` to set request header and `-d` to set request data.

An example of sending a `PUT` request:

```console
$ curl -X PUT -H 'Content-Type: application/json' -d '{"key": "value"}' localhost:8080/index/doc/42
```

When using URL with query string like `localhost:8080/foo?key1=value1&key2=value2`, the parameter after `&` will be truncated because shell sees it as the end of a command. In this case, the URL string must be quoted.

## Authentication

Basic auth:

```console
$ curl -u <username>:<password>
```

## Output

Display verbose logging:

```console
$ curl -v localhost:8080
```

Use `-I` or `--head` option to get the document info like:

```
HTTP/2 200
date: Thu, 04 Jul 2019 10:12:58 GMT
content-type: application/json;charset=UTF-8
content-length: 91
expires: 0
cache-control: no-cache, no-store, max-age=0, must-revalidate
x-xss-protection: 1; mode=block
pragma: no-cache
x-frame-options: DENY
x-content-type-options: nosniff
strict-transport-security: max-age=15724800
```

But since it's a POST request itself, it can't be used together with another POST request. In the POST case, use `-i` (`--include`) instead to print protocol response headers (incl. response body) like:

```
HTTP/2 200
date: Thu, 04 Jul 2019 10:12:21 GMT
content-type: application/json;charset=UTF-8
vary: Accept-Encoding
expires: 0
cache-control: no-cache, no-store, max-age=0, must-revalidate
x-xss-protection: 1; mode=block
pragma: no-cache
x-frame-options: DENY
x-content-type-options: nosniff
strict-transport-security: max-age=15724800
{
  // response body
}
```

Use `-o <file>` or `> <file>` to write the output to a file.

### Advanced

To send a request repeatedly for a given number of times, e.g. 3 times:

```console
$ curl localhost:8080?[1-3]
```

If there are query parameters in the URL, append it with a dummy query key like:

```console
$ curl localhost:8080?val=42&dummy=[1-3]
```

To send requests continuously over a given internal, an option is to use `watch`:

```console
$ watch -n <sec> curl localhost:8080
```
