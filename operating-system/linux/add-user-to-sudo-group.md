# Add User to `sudo` Group

On Debian/Ubuntu, use `su -` to get the root access and then run the following command to add an existing user to `sudo` group:
 
```console
$ sudo adduser <username> sudo
```

List all users in the `sudo` group:

```console
$ grep -Po '^sudo.+:\K.*$' /etc/group
```
