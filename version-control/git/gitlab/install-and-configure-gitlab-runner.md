# Install and Configure GitLab Runner

1. On Ubuntu, download and install the latest package:

  ```console
  $ curl -LJO https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb
  $ sudo dpkg -i gitlab-runner_amd64.deb
  ```

2. Obtain a registration token from `Settings > CI / CD > Runners > Specific Runners > Set up a specific Runner manually`

3. Register GitLab Runner with the token:

  ```console
  $ sudo gitlab-runner register
  ```

4. After registration, the active runner should appear in `Settings > CI / CD > Runners > Runners activated for this project`.


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
