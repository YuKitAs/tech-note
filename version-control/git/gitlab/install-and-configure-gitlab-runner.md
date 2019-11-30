# Install and Configure GitLab Runner

## Set up a Specific Runner

1. On Ubuntu, download and install the latest package of `gitlab-runner`:

  ```console
  $ curl -LJO https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb
  $ sudo dpkg -i gitlab-runner_amd64.deb
  ```

2. Obtain a registration token from `Settings > CI / CD > Runners > Specific Runners > Set up a specific Runner manually`

3. Register GitLab Runner with the token:

  ```console
  $ sudo gitlab-runner register
  ```

4. After registration, the runner should appear in `Settings > CI / CD > Runners > Runners activated for this project` and it will be active by default.

5. By default, the runner should be tagged because it's only allowed to run [tagged jobs](https://docs.gitlab.com/ee/ci/yaml/README.html#tags). To change this behavior, edit the runner by enabling `Run untagged jobs`, so that untagged jobs as well as the jobs tagged with specific tags can be picked up by the runner.


## Useful Commands

* List all configured runners (registered and unregistered):

  ```console
  $ sudo gitlab-runner list
  ```

* Unregister a runner:

  ```console
  $ sudo gitlab-runner unregister --url https://gitlab.com --token <token>
  ```

* Delete runners that are removed from GitLab:

  ```console
  $ sudo gitlab-runner verify --delete
  ```
