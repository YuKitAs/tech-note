# Get Messages from Queue

1. Enable management plugins:

  ```console
  $ rabbitmq-plugins enable rabbitmq_management
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

2. Install `rabbitmqadmin` tool:

  Open `http://localhost:15672/cli/rabbitmqadmin`, copy the whole script into `/usr/local/bin/rabbitmqadmin` and make it executable

3. Run the following command to get messages from a queue, but pay attention, this is a destructive action:

  ```console
  $ rabbitmqadmin get queue=<queue-name>
  ```
