# Run Docker Without `sudo`

The Docker daemon always run as the `root` user, the other users can only access it using `sudo`. If running `docker-compose` without `sudo`, it won't be able to connect to the Docker daemon due to permission problem. To avoid using `sudo` to execute `docker` command every time, we can add the user to a `docker` Unix group.

1. Check if the `docker` group already exists:

  ```console
  $ cat /etc/group | grep docker:
  ```

  If not, create it:

  ```console
  $ sudo groupadd docker
  ```

2. Add the current user to the `docker` group:

  ```console
  $ sudo usermod -aG docker $USER
  ```

3. Log out and log in, or re-evaluate the group members from inside the shell (see [note](https://github.com/YuKitAs/tech-note/blob/master/operating-system/linux/users-and-sudo-group.md))

4. Run the `hello-world` image to verify:

  ```console
  $ docker run hello-world
  ```
