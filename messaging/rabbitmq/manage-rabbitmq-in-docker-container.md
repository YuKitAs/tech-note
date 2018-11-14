# Manage RabbitMQ in Docker Container

1. Pull and run RabbitMQ image:

  ```console
  $ docker pull rabbitmq
  $ docker run -p 5671:5671 -p 5672:5672 -p 15672:15672 -d rabbitmq
  ```

2. Enable `rabbitmq-management` in the Docker container where the `rabbitmq` image is running:

  ```console
  $ docker exec <container-ID|container-name> rabbitmq-plugins enable rabbitmq_management
  ```

3. Go to visit `http://localhost:15672`, login with username `guest` and password `guest`
