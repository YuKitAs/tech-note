# Common Use Cases of HTTP Status Codes

The following choices are based on personal understanding and experiences in implementing HTTP servers.

## 2xx Success

**200 OK** - Used for a successful request, usually the server will return the result of the action.

**201 Created** - Used for a POST request for creating a new resource.

**204 No Content** - Similar to 200 but the server does not return anything, e.g. for a successful DELETE request.

## 4xx Client errors

**400 Bad Request** - Used when the server cannot process the request due to apparent client errors like incorrect request syntax.

**401 Unauthorized** - Used when authentication is required.

**403 Forbidden** - Similar to 401, used when authentication is provided but the user doesn't have the right permission.

**404 Not Found** - Usually used for a GET request with e.g. a wrong id.

**409 Conflict** - Used when the request cannot be processed due to conflicting condition, e.g. to delete an entity that does not exist.

**422 Unprocessable Entity** - Similar to 400, used when the request syntax is correct but the request cannot be processed due to semantic errors.

## 5xx Server errors

**500 Internal Server Error** - Used when an unexpected condition was encountered
