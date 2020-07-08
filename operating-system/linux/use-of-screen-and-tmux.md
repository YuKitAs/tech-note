# Use of `screen` and `tmux`

`screen` and `tmux` are terminal multiplexers for managing multiple long-running processes that can be detached and reattached.

Basic commands:

|   |`screen`|`tmux`|
|---|:---|:---|
|Detach|`Ctrl + A` and `D`|`Ctrl + B` and `D`|
|List all sessions|`screen -ls`|`tmux ls`|
|Reattach|`screen -r <session-id>`|`tmux attach-session -t <session-id>`|
|Kill detached session|`screen -S <session-id> quit`|`tmux kill-session -t <session-id>`|
