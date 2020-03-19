# Send HTTP Requests

Install and import `requests` library:

```python
import requests
```

## Requests

```python
response = requests.get(url, params, headers)
response = requests.post(url, params, json, headers)
response = requests.put(url, params, json, headers)
response = requests.delete(url, params, headers)
```
where `params`, `json` (used to be `data`) and `headers` are optional dictionaries like:

```python
{'key1': 'value1', 'key2': ['value2', 'value3']}
```

Example:
```python
requests.post('example.com', data=json.dump({'key': 'value'}), headers={'Content-Type': 'application/json'})
```

## Responses

* Response status code

```python
if response.status_code == 200:
  print('Success')
```

* Response body

```python
# Content in bytes
response.content
# Content in string
response.text
# Content in JSON
response.json()
```

## Exception handling

```python
from requests.exceptions import HTTPError

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    # handle 4xx or 5xx error response
except Exception as err:
    # handle other exceptions
else:
    print('Success!')
```
