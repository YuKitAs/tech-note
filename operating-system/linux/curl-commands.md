# `curl` Commands

## Request

`curl` commands are frequently used to test RESTful web services. One of the most useful commands is:

```console
$ curl -X <method>
```

where method could be `GET`, `POST`, `PUT` or `DELETE`.

Use `-H` to set request header and `-d` to set request data.

An example of sending a `PUT` request:

```console
$ curl -X PUT -H 'Content-Type: application/json' -d '{"key": "value"}' localhost:8080/index/doc/42
```

When using URL with query string like `localhost:8080/foo?key1=value1&key2=value2`, the parameter after `&` will be truncated because shell sees it as the end of a command. In this case, the URL string must be quoted.

## User

Basic authentication:

```console
$ curl -u <username>:<password>
```

## Logging

Use verbose logging to make the operation more talkative:

```console
$ curl -v http://localhost
```
