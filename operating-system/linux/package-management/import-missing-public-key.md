# Import Missing Public Key

On Debian/Ubuntu, when the Apt system doesn't have the public key it needs to install a package, we will get warnings like `The following signatures couldn't be verified because the public key is not available: NO_PUBKEY <key_id>`. To fix it, we can download and import the missing PUBKEY manually with:

```console
# apt-key adv --keyserver <server> --recv-key <key_id>
```

`apt-key` is the program that manages a keyring of gpg keys. There are different servers that can be chosen, like `keyserver.ubuntu.com` or `ipv4.pool.sks-keyservers.net`.

Refresh keys for all packages:

```
# apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com
```
