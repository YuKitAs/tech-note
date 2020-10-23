# Update `npm` and `Node.js`

## Install with [`nvm`](https://github.com/nvm-sh/nvm) (Node Version Manager)

It's the recommended way to avoid permission errors when installing packages globally.

Download and install `nvm`:

```console
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash
```

Source the current profile file or open a new terminal to verify the installation:

```console
$ nvm -v
```

Install the latest release of `node` or a specific version:

```console
$ nvm install node
$ nvm install 14.14.0
```

List available `node` versions:

```console
$ nvm ls-remote
```

List installed `node` versions:

```console
$ nvm ls
```

Use an available `node` version:

```console
$ nvm use 14.14.0
```

## Install without `nvm`

Download and install `nodejs`:

```console
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Check the versions of `npm` and `node`:

```console
$ npm --version
$ node --version
```

Update `npm`:

```console
$ npm i -g npm
```

Update `Node.js`:

```console
$ npm cache clean
$ npm update -g
```

For `EACCES: permission denied` errors, change owner of the following directories to the current user:

```console
$ sudo chown -R $USER /usr/local/lib/node_modules/
$ sudo chown -R $USER /usr/local/bin/
```
