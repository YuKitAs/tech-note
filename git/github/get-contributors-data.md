# Get Contributors Data

Use the following command to get the contributors list with additions, deletions and commit counts based on weeks with the help of [GitHub REST API](https://developer.github.com/v3/repos/statistics/), and save into JSON file:

```console
$ curl -XGET https://api.github.com/repos/{owner}/{repo}/stats/contributors > contributors-data.json
```

The same JSON can also be easily achieved when visiting `https://github.com/{owner}/{repo}/graphs/contributor`. Just select a time period, open `Developer Tools > Network`, refresh the page and check the response for `contributors-data`.
