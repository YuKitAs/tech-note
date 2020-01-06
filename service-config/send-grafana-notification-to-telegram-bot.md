# Send Grafana Notification to Telegram Bot

1. Add Telegram Bot to a group chat.

2. Get chat id (e.g. `-123456789`) by sending a dummy message to the bot - either check `https://api.telegram.org/bot<bot-api-token>/getUpdates`, or directly check the debug logs of the bot.

3. On Grafana, create a new Notification Channel (`/alerting/notification/new`). Choose `Telegram` as type, enter Bot API Token and Chat ID. Send a test notification.

4. In the Dashboard settings, create a new Alert, define Rule, Conditions, Notifications etc.
