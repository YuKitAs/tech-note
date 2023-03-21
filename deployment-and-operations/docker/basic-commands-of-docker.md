# Basic Commands of Docker

## Common

* **List all Docker commands**:

  ```console
  $ docker
  ```

* **Show Docker version and info**:

  ```console
  $ docker --version
  $ docker info
  ```

* **Show usage of a Docker command**:

  ```console
  $ docker <command> --help
  ```

## Docker Image

* **Build a Docker image (for the current project)**:

  ```console
  $ docker build -f <path/to/Dockerfile> -t <image-tag> .
  ```

* **List all Docker images**:

  ```console
  $ docker images
  ```

* **Run a Docker image in a new container**:

  ```console
  $ docker run <image-ID|image-name>
  ```

* **Run a Docker image and enter the newly created container**:

  ```console
  $ docker run -it <image-ID|image-name> bash
  ```

  `-it` means interactively.

* **Remove a Docker image**:

  ```console
  $ docker rmi <image-ID>
  ```

* **Remove all Docker images**:

  ```console
  $ docker rmi $(docker images -q)
  ```

  `-q` means only displaying IDs.

  or

  ```console
  $ docker images -q | xargs docker rmi
  ```

  Add `-f dangling=true` to only remove dangling/untagged images.
  
* **Show history of a Docker image**:

  ```console
  $ docker history <image-ID|image-name>
  ```

## Docker Container

* **List running Docker containers**:

  ```console
  $ docker ps
  ```

* **List all Docker containers**:

  ```console
  $ docker ps -a
  ```

* **Start a Docker container**:

   ```console
   $ docker start <container-ID|container-name>
   ```

* **Stop a Docker container**:

  ```console
  $ docker stop <container-ID|container-name>
  ```

* **Stop all containers**:

  ```console
  $ docker stop $(docker ps -aq)
  ```

* **Remove a Docker container**:

  ```console
  $ docker rm <container-ID>
  ```

* **Remove all Docker containers**:

  ```console
  $ docker rm $(docker ps -aq)
  ```

* **Remove all stopped containers**:

  ```console
  $ docker ps -aq --no-trunc -f status=exited | xargs docker rm
  ```
  
  ```console
  $ docker container prune
  ```

* **Execute commands in a running container**:

  ```console
  $ docker exec <container-ID|container-name> <command>
  ```

* **Enter a running container as root (start an interactive Bash session)**:

  ```console
  $ docker exec -it <container-ID|container-name> bash
  ```

* **Copy files from host into container**:

  ```console
  $ docker cp /path/to/file <container-ID>:/path/to/file
  ```
  
* **Copy files from container to host**:

  ```console
  $ docker cp <container-ID>:/path/to/file /path/to/file
  ```

* **Output logs for a running container**:

  ```console
  $ docker logs -f <container-ID>
  ```

  `-f` means following logs.


* **Show IP address of a Docker container**:

  ```console
  $ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-ID|container-name>
  ```

  `-f` is short for `--format`.

## Docker Volume

* **List all volumes**:

  ```console
  $ docker volume ls
  ```

* **Remove all dangling volumes** (stored in `/var/lib/docker/volumes`):

  ```console
  $ docker volume rm $(docker volume ls -f dangling=true)
  ```
  
  or
  
  ```console
  $ docker volume prune
  ```
  
## Docker System

* **Remove all unused and dangling images, containers, networks and build cache (`volumes` need to be given explicitly)**:

  ```console
  $ docker system prune -a -f [--volumes]
  ```

## Docker Compose

* **Build and run a container with services defined in** `docker-compose.yml`:

  ```console
  $ docker-compose up
  ```

  Add `-d` to make containers run in the background.

* **Stop containers and remove containers, networks, volumes and images created with** `docker-compose`:

  ```console
  $ docker-compose down
  ```
