# Send Grafana Notification to Telegram Bot


1. Get Bot API Token from BotFather

2. Get Chat ID:

  2.1 ... of a user:

  * Send a message to the bot

  * Call `https://api.telegram.org/bot<token>/getUpdates`

  2.2 ... of a group:

  * In Bot settings, disable `Group Privacy` so that the Bot can have access to group messages

  * Create a group and add the Bot to the group

  * Send a message in the group

  * Call `https://api.telegram.org/bot<token>/getUpdates`

2. Send a test request:

  ```
  https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>d&text=test
  ```

3. On Grafana, create a new Notification Channel (`/alerting/notification/new`). Choose `Telegram` as type, enter Bot API Token and Chat ID. Send a test notification.

4. In the Dashboard settings, create a new Alert, define Rule, Conditions, select Notifications etc.
