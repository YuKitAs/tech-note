# Use of Personal Access Token

The personal access token can be used for applications that needs access to the GitLab API. For example, it can be used for `docker login` when accessing container registry images on GitLab.

The token can be generated via `User Settings > Access Tokens`.

Copy the generated token and use for `docker login`:

```console
$ docker login <registry> -u gitlab-ci-token -p <token>
```
