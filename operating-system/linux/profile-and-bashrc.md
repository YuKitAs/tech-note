# `.profile` and `.bashrc`

`.profile` and `.bashrc` are both shell config files. The main differences are, `.profile` is read by login shells and is usually used to configure environment variables, while `.bashrc` is specific to `Bash` and is only read by interactive and non-login shells, so it's used to configure `Bash` usage like `alias`.

In addition, `.bash_profile` is a personal initialization file which is also read by login shells, but when it exists, it'll be read before the system-wide config file `.profile`. So when using `.bash_profile`, make sure to include `.profile` like:

```
. ~/.profile
```

Otherwise `.profile` will be omitted.
