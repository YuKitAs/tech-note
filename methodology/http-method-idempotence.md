# HTTP Method Idempotence

**Idempotent methods**: the result of a successful performed request is independent of the number of times it is executed.

**Safe methods**: methods that can be cached, prefetched without any repercussions to the resource.

| Method | Idempotent | Safe |
|---|---|---|
| GET | Yes | Yes |
| HEAD | Yes | Yes |
| POST | No | No |
| PUT | Yes | No |
| PATCH | No | No |
| DELETE | Yes | No |

\* According to [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH), `PATCH` **can be** idempotent, but successive identical patch requests **may** have different effects, thus it's considered to be non-idempotent.

Example for a `PATCH` request:

```
{
  $increment: "age"
}
```

Clearly, the `age` field of the resource will be modified each time when the request is executed, so it's not idempotent.
