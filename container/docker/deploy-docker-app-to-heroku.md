# Deploy Docker App to Heroku

Deploy Docker-based app with `Container Registry` deployment method using Heroku CLI.

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

2. Log in to Heroku account

  ```console
  $ heroku login
  ```

3. Set up Docker locally and sign into Container Registry:

  ```console
  $ heroku container:login
  ```

4. Create `Dockerfile` in the app and push the Docker image:

  ```console
  $ heroku container:push web -a <heroku-app-name>
  ```

5. Release the pushed image:

  ```console
  $ heroku container:release web -a <heroku-app-name>
  ```

6. Watch app logs:

  ```console
  $ heroku logs --tail -a <heroku-app-name>
  ```
