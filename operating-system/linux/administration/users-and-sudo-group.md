# Users and `sudo` Group

In order for a user to run `sudo` (get `root` privileges to execute some commands without being `root`), the user must belong to the `sudo` group. 

## Add a user to `sudo` group

On Debian/Ubuntu, use `su -` to get the root access and then run the following command to add an existing user to `sudo` group:
 
```console
$ adduser <username> sudo
```

The following command is used to check which groups the current user belongs to:

```console
$ groups
```

Re-evaluate group members:

```console
$ su - $USER
$ id
```

## List all local users

```console
$ cat /etc/passwd
```

The output, e.g. `root:x:0:0:root:/root:/bin/bash` contains information about user ID, group ID, full name of the user, user home directory and login shell.

## List all users in `sudo` group

```console
$ grep -Po '^sudo.+:\K.*$' /etc/group
```

## Reference

* [debian WIKI](https://wiki.debian.org/sudo)
