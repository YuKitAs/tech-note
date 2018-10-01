# Import Missing Public Key

On Ubuntu, when the Apt system doesn't have the public key it needs to install a package, we will get warnings like `The following signatures couldn't be verified because the public key is not available: NO_PUBKEY <key_id>`. To fix it, we can download and add the missing PUBKEY manually with:

```console
# apt-key adv --keyserver keyserver.ubuntu.com --recv-key <key_id>
```
