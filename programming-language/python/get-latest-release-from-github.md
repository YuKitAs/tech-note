# Get Latest Release from Github

First of all, verify if we can list all the tag infos with `curl`:

```console
$ curl -s https://api.github.com/repos/<username>/<reponame>/tags
```

If it works, all tags should be returned in descending order, which means the first object contains the information of the latest release. We can then do more things with it using Python. The following script requires modules `requests` and `json`.

```python
import requests, json

url = "https://api.github.com/repos/<username>/<reponame>/tags"
version = requests.get(url).json()[0]["name"]
print("Latest release: {}".format(version))
```
