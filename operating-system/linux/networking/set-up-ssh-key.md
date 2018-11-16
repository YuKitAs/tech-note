# Set up SSH Key

Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.

With SSH keys we can connect and authenticate to remote servers and services through command-line login and execute remote commands.

## Generate SSH key

By default, the public/private SSH key pair will be stored in `~/.ssh`, so we can check whether the SSH keys already exist - whether there are two files `id_rsa` (for private identification) and `id_rsa.pub` (for pubic key) in `~/.ssh`.

To generate a new random key pair, we can simply use the command `ssh-keygen`.

The default key size is 2048, we could choose to specify a bigger (and thus safer) size using the `-b` option like:

```console
$ ssh-keygen -t rsa -b 4096
```

After leaving all the default answers for prompts, a key fingerprint, a key's randomart image as well as `~/.ssh/id_rsa` and `.ssh/id_rsa.pub` will be generated.

Besides, an account name (e.g. GitHub email address) can be specified with the `-C` option like:

```console
$ ssh-keygen -C "yukitas@example.com"
```

## Test SSH connection

Copy the whole content of `id_rsa.pub` and add it to a remote server.

Try to use the following command:

```console
$ ssh -T <name>@<host>
```
For the warning, enter "yes" to continue connection. On success we would be authenticated.

## SSH agent

`ssh-agent` is a helper program that keeps track identity keys and passphrases.

To add the SSH private key to the `ssh-agent`, start the `ssh-agent` in the background and use `ssh-add`:

```
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
```

## Copy public keys

The public key can be copied to remote host using the following command:

```console
$ ssh-copy-id <username>@<host>
```

## Reference

* [SSH-KEYGEN - GENERATE A NEW SSH KEY](https://www.ssh.com/ssh/keygen/)
