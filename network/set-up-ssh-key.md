# Set up SSH Key

By default, the public/private SSH key pair will be stored in `~/.ssh`, so we can check whether the SSH keys already exist.

To generate a new random key pair, we can simply use the command `ssh-keygen`. 

The default key size is 2048, but we can specify a bigger (and thus safer) size using the `-b` option like:

```console
$ ssh-keygen -t rsa -b 4096
```

Besides, an account name (e.g. GitHub email address) can be specified with the `-C` option like:

```console
$ ssh-keygen -C "yukitas@example.com"
```

To add the SSH private key to the `ssh-agent` (so that we don't have to enter password for the account every time), start the `ssh-agent` in the background and use `ssh-add`:

```
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
```

The public key can be copied to remote host using the following command:

```console
$ ssh-copy-id <username>@<host>
```

## Reference

* [SSH-KEYGEN - GENERATE A NEW SSH KEY](https://www.ssh.com/ssh/keygen/) 
