import sys
import requests, json

# https://api.github.com/repos/<username>/<repo>

repo_url = "https://api.github.com/repos/{}/{}".format(sys.argv[1], sys.argv[2])
response = requests.get(repo_url + "/tags").json()
if response:
    print("Latest release: {}".format(response[0]["name"]))
else:
    print("No release found for {}".format(repo_url))
