# Send Grafana Notification to Telegram Bot

1. Get Bot API Token and chat id (e.g. `123456789`) with the bot. A test request:

```
https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>d&text=test
```

2. On Grafana, create a new Notification Channel (`/alerting/notification/new`). Choose `Telegram` as type, enter Bot API Token and Chat ID. Send a test notification.

3. In the Dashboard settings, create a new Alert, define Rule, Conditions, select Notifications etc.
