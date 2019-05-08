# Shell Options

## `set`

Originally, `set` can be used to set/unset shell options.

List all current settings:

```console
$ set -o
```

To enable (set) an option:

```console
$ set -o <option>
```

For example, use `set -o ignoreeof` to prevent exiting the login shell with `Ctrl+D`.

To disable (unset) an option:

```console
$ set +o <option>
```

## `shopt`
`shopt` is used to set/unset Bash-specific shell options.

List all current settings:

```console
$ shopt
```

To enable (set) an option:

```console
$ shopt -s <option>
```

For example, use `shopt -s dotglob` to list hidden `.*` files.

To disable (unset) an option:

```console
$ shopt -u <option>
```
