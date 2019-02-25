# Use of `screen`

`screen` is useful for long-running process that can be detached and reattached.

By running the command `screen` we will get into a new sub-shell and there we can run any process.

* Detach from the screen with it still running: `Ctrl + A` and `Ctrl + D`

* Reattach: `screen -r <session-name>`

* List all available screen sessions: `screen -list`
