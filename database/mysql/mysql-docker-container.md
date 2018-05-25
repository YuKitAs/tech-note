# MySQL Docker Container

1. Pull the latest [`mysql`](https://hub.docker.com/_/mysql/) image from Docker Hub:

  ```console
  $ docker pull mysql
  ```

2. Start a MySQL instance by specifying a name to the container, a password for the MySQL root user and the MySQL version:

  ```console
  $ docker run --name <container_name> -e MYSQL_ROOT_PASSWORD=n0password -d mysql
  ```

  Optionally create a database by adding `-e MYSQL_DATABASE=<db_name>`.

  On success the container ID will be printed to the console.

  Use `docker ps` to verify if the container is running.

3. Use the following command to start a `mysql` client inside the container we have just started:

  ```console
  $ docker exec -it <container-name> mysql -u root -p
  ```

  Enter the password and we should be in the MySQL command line client like:

  ```console
  mysql>
  ```
