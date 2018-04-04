# Install and Setup Go on Ubuntu

1. After `apt update` and `apt upgrade`, download the latest version from the [official website](https://golang.org/dl/).

2. Extract the files with `tar -xvf` and move the `go` folder into `/opt`.

3. Set `GOROOT` and `GOPATH` by adding the following commands to the end of `~/.profile`:

  ```text
  export GOROOT="/opt/go"
  export GOPATH="$HOME/.go"
  export PATH="$PATH:$GOROOT/bin:$GOPATH:bin"
  ```

  `GOROOT` specifies where Go is installed. `GOPATH` specifies the location of workspace, so we can create a empty folder like `$HOME/.go`.

4. Restart the terminal or run `source ~/.profile`. Then use `echo $PATH` to check whether the environment variables are set correctly.

5. Verify installation by running `go version` and `go env`.

When using `go get` to fetch some packages, there will be an error:

```console
exec: "hg": executable file not found in $PATH
```

It means we need to install Mercurial revision control system first. Install Mercurial with `apt install mercurial` and run `hg version` to verify installation.
