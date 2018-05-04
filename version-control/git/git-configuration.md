# Git Configuration

There are three configuration levels: local (repository-specific settings), global (user-specific settings) and system. Git stores local configurations in `<repo>/.git/config`, global configurations in `~/.gitconfig`, system configurations in `/etc/gitconfig`.

We can use `--local | --global | --system` flag to set the configuration for a specific level like:

```console
$ git config --global user.name "YuKitAs"
$ git config --global user.email YuKitAs@example.com
```
