# Set up SSH Key

In console, run `ssh-keygen` to generate random public/private rsa key pair. By default they will be saved in `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`.

The default key size is 2048 but we can specify a size by using the `-b` option like:

```console
$ ssh-keygen -t rsa -b 4096
```

The public key can be copied to remote host using the following command:

```console
$ ssh-copy-id <username>@<host>
```

## Reference

* [SSH-KEYGEN - GENERATE A NEW SSH KEY](https://www.ssh.com/ssh/keygen/) 
