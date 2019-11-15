# Install Community Plugins

1. Download the plugin from the [list](https://www.rabbitmq.com/community-plugins.html)

2. Copy the `.ez` file into `/usr/lib/rabbitmq/lib/rabbitmq_server-<version>/plugins/`

3. Enable the plugin:

  ```console
  $ sudo rabbitmq-plugins enable <plugin-name>
  ```
