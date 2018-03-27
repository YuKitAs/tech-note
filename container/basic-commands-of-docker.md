# Basic Commands of Docker

* **List all Docker commands**:

  ```console
  $ docker
  ```

* **Show Docker version and info**:

  ```console
  $ docker --version
  $ docker info
  ```

* **Show Docker daemon status**:

  ```console
  $ sudo service docker status
  ```

* **List all Docker images**:

  ```console
  $ docker image ls
  ```
  
  or
  
  ```console
  $ docker images
  ```

* **Execute a Docker image**:

  ```console
  $ docker run <image-ID|image-name>
  ```
  
* **Enter a Docker image and run commands interactively**:

  ```console
  $ docker run -it <image-ID|image-name> bash
  ```

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

  Add `--filter dangling=true` to only remove dangling/untagged images.

* **List running Docker containers**:

  ```console
  $ docker container ls
  ```

  or

  ```console
  $ docker ps
  ```

* **List all Docker containers**:

  ```console
  $ docker container ls --all
  ```

  or

  ```console
  $ docker ps -a
  ```

* **Remove a Docker container**:

  ```console
  $ docker rm <container-ID>
  ```

* **Remove all Docker containers**:

  ```console
  $ docker rm $(docker ps -aq)
  ```

  or

  ```console
  $ docker ps -aq | xargs docker rm
  ```

  Add `--no-trunc` parameter to only remove stopped containers.
  
* **Build and run a container with services defined in** `docker-compose.yml`:

  ```console
  $ docker-compose up
  ```
  
  Add `-d` to make containers run in the background.
  
* **Stop containers and remove containers, networks, volumes and images created with** `docker-compose`:

  ```console
  $ docker-compose down
  ```

* **Run commands in a running container**:

  ```console
  $ docker exec <container-ID|container-name> <command>
  ```

* **Enter a running container as root**: 

  ```console
  $ docker exec -it <container-ID|container-name> bash
  ```

* **Exit a container**: `ctrl + p` and then `ctrl + q`
