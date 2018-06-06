# Users and `sudo` Group

In order for a user to run `sudo` (get `root` privileges to execute some commands without being `root`), the user must belong to the `sudo` group. 

## Add user to `sudo` group

On Debian/Ubuntu, use `su -` to get the root access and then run the following command to add an existing user to `sudo` group:
 
```console
$ adduser <username> sudo
```

The following command is used to check which groups the current user belongs to, `sudo` should now be printed as one of them:

```console
$ groups
```

## List all users in `sudo` group

```console
$ grep -Po '^sudo.+:\K.*$' /etc/group
```

## Reference:

* [debian WIKI](https://wiki.debian.org/sudo)
