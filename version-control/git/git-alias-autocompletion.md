# Git Alias Auto-Completion

When defined aliases for Git like `alias gco='git checkout'`, the auto-completion by tab won't work any more. A quick fix is to make use of the `bash-completion`.

1. Add the following Bash codes into `~/.bash_aliases` or `~/.bashrc`:

  ```bash
  if [ -f "/usr/share/bash-completion/completions/git" ]; then
    . /usr/share/bash-completion/completions/git
    __git_complete gco _git_checkout
  fi
  ```

  `__git_complete` is a Bash completion build-in function for Git. To use it we have to source `/usr/share/bash-completion/completions/git`. The function format is like

  ```
  __git_complete <git_alias> _git<_command>
  ```

2. Source `~/.bashrc`. Then we can checkout a branch by auto-completing the branch name with Git alias:

  ```console
  $ gco <tab>
  ```
