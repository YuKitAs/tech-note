# Install RabbitMQ Management Plugin

1. Make sure the `rabbitmq-server` service is running.

2. Enable management plugins:

  ```console
  $ sudo rabbitmq-plugins enable rabbitmq_management
  ```

  The following plugins will be enabled:

  ```
  mochiweb
  webmachine
  rabbitmq_web_dispatch
  amqp_client
  rabbitmq_management_agent
  rabbitmq_management
  ```

  Check if we can visit the management UI `http://localhost:15672`.

3. Install `rabbitmqadmin` tool by downloading the script and making it executable:

  ```console
  $ curl -O http://localhost:15672/cli/rabbitmqadmin && sudo mv rabbitmqadmin /usr/local/bin/rabbitmqadmin
  $ sudo chmod a+x /usr/local/bin/rabbitmqadmin
  ```
