# `curl` Commands

`curl` commands are frequently used to test RESTful web services. One of the most useful commands is:

```console
$ curl -X <method>
```

where method could be `GET`, `POST`, `PUT` or `DELETE`.

Basic authentication:

```console
$ curl -u <username>:<password>
```

Use `-H` to set request header and `-d` to set request data.

An example of sending a `PUT` request:

```console
$ curl -X PUT -H 'Content-Type: application/json' -d '{"key": "value"}' localhost:8080/index/doc/42
```
