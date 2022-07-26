# Set up Local Web Server

If local files can't be accessed in browser with `file://` for any reason, we would need a local web server.

* With Python3, run

```console
$ python -m http.server
```

to start a local web server at `localhost:8000` inside the directory with the files to serve.

* With Node, install the `http-server` package globally and run:

```console
$ npm i -g http-server
$ http-server
```

to start a local web server at `localhost:8081` inside the directory with the files to serve.
