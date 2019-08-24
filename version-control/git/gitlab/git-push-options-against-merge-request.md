# Git Push Options Against Merge Request

GitLab supports `git push -o` with the following actions when pushing changes (since 11.10):

* Create a new merge request for the pushed branch:

  ```
  merge_request.create
  ```

* Set target branch:

  ```
  merge_request.target=<branch_name>
  ```

* Merge when pipeline succeeds:

  ```
  merge_request.merge_when_pipeline_succeeds
  ```

* Remove source branch when the MR is merged:

  ```
  merge_request.remove_source_branch
  ```

* Set MR title and description:

  ```
  merge_request.title="<title>"
  merge_request.description="<description>"
  ```

A simple example:

```console
$ git push -o merge_request.create -o merge_request.merge_when_pipeline_succeeds -o merge_request.remove_source_branch
```
