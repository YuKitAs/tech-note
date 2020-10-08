# Send Mattermost Messages with Bot

With admin right in the team, create an `Incoming Webhook` in `Integrations`, which would look like this

```
https://<mattermost-url>/hooks/<generated-key>
```

Then we can just send a POST request to the URL above with the following request bodies:

* send a message to a channel in the team:

  ```json
  {
    "channel": "town-square",
    "text": "test test :tada:"
  }
  ```

  If no `channel` specified, the message will be sent to the default channel specified while creating the webhook.

* send a direct message to a user:

  ```json
  {
    "channel": "@username",
    "text": "test test :tada:"
  }
  ```

The default bot is called `webhook` with a default profile image. Optionally we can specify a bot name and its profile image by adding the following fields:

```json
{
  "username": "Tooluser",
  "icon_url": "https://image.png"
}
```
