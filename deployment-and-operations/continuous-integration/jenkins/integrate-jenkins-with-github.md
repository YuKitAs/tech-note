# Integrate Jenkins with Github

1. Install Jenkins:

  ```console
  $ wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
  $ sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
  $ sudo apt update
  $ sudo apt update install jenkins
  ```

2. Get Jenkins admin password:

  ```console
  $ sudo cat /var/lib/jenkins/secrets/initialAdminPassword
  ```

3. Visit Jenkins instances root page on `localhost:8080`, enter the copied password to login.

4. Install suggested plugins and create an admin account.

5. Go to `Manage Jenkins > Manage Plugins > Installed`, the `Github plugin` should be already installed, if not search for and install it.

6. Go to `New Item (Element anlegen)`, enter an item name (something like "Github project"), choose `Freestyle project`.

7. In `General`, choose `GitHub Project` and enter a project URL.

8. Under `Source Code Management`, choose `Git` and enter the Git repo URL (\*.git) with credentials.

9. Under `Build Triggers (Build-Auslöser)`, choose `GitHub hook trigger for GITScm polling` and save.

10. On GitHub, go to `Settings > Developer settings`, generate a new personal access token.

11. Go to `Manage Jenkins > Configure System`, add a `GitHub Server` with `https://api.github.com` as default `API URL`. Add credentials, copy the access token as `Secret text` and click `Test connection`. If verified, select `Manage hooks` and save. The webhook in GitHub should have been configured by Jenkins automatically.
