# `.profile`, `.bashrc` and `.bash_profile`

* `~/.profile`: system-wide initialization file, executed for **interactive login shells**, usually used to configure environment variables. `~/.profile` will include `~/.bashrc` by default if that exists, but won't be read if `~/.bash_profile` or `~/.bash_login` exists.

* `~/.bashrc`: individual per-interactive-shell startup file, specific to Bash and is only read by **interactive and non-login shells**, so it's used to configure Bash usage, e.g. color support or aliases as follows:

  ```
  alias ll='ls -alF'
  alias la='ls -A'
  alias l='ls -CF'
  ```

* `~/.bash_profile`: personal initialization file which is only read by **interactive login shells**. When using `~/.bash_profile`, make sure to source `~/.profile` and `~./bashrc` there like:

  ```
  . ~/.profile
  . ~/.bashrc
  ```

Whether a Bash shell is started as a login shell can be checked with:

```console
$ shopt login_shell
```

When seeing `login_shell off`, normally it means `~/.bash_profile` won't be executed. It's better to place environment variables in `~/.profile` since on Ubuntu it will get executed during the start-up process desktop session as well as by the login shell.
