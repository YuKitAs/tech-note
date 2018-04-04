# Install and Setup Go on Ubuntu

1. After `apt update` and `apt upgrade`, download the latest Go release from the [official website](https://golang.org/dl/).

2. Extract the files with `tar -xvf` and move the `go` folder into `/opt`.

3. Set `GOROOT` and `GOPATH` by adding the following commands to the end of `~/.profile`:

  ```text
  export GOROOT="/opt/go"
  export GOPATH="$HOME/.go"
  export PATH="$PATH:$GOROOT/bin:$GOPATH:bin"
  ```

  `GOROOT` specifies where Go is installed. `GOPATH` specifies the location of workspace, here we create an empty directory called `$HOME/.go` to be used as `GOPATH`. The default `GOPATH` is `$HOME/go`.

4. Restart the terminal or run `source ~/.profile`. Then use `echo $PATH` to check whether the environment variables are set correctly.

5. Verify installation by running `go version` and `go env`.

## Use Go Packages

`go get <go-package>` is used to download packages and save them under `$GOPATH/src`.

When using `go get` to fetch some packages, we might see an error:

```console
exec: "hg": executable file not found in $PATH
```

It means we need to install Mercurial revision control system first. Install Mercurial with `apt install mercurial` and run `hg version` to verify installation.

After successfully downloaded the package, if we want to run it as a standalone executable, we can use `go build <go-package>` to create an executable in the current directory, or use `go install <go-package>` to create an executable in `$GOPATH/bin`.
