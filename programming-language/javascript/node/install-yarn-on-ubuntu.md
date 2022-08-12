# Install Yarn on Ubuntu

1. Add Yarn via Debian package repository:

  ```console
  $ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
  $ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
  ```

2. Update and install:

  ```console
  $ sudo apt update && sudo apt install yarn
  ```

3. Check the version:

  ```console
  $ yarn --version
  ```

The directory where Yarn stores global packages can be found with:

```console
$ yarn global dir
```
By default it's `~/.config/yarn/global` or `/usr/local/share/.config/yarn/global` for root user.

The directory where Yarn stores global binaries can be found with:

```console
$ yarn global bin
```
By default it's `~/.yarn/bin` or `/usr/local/bin`. Make sure the output path is added into `$PATH`.
