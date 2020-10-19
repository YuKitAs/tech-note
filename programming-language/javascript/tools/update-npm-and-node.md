# Update `npm` and `Node.js`


Install Node.js on Ubuntu:

```console
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Check the versions of `npm` and `Node.js`:

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
