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

4. Restart the terminal and use `echo $PATH` to check whether the environment variables are set correctly.

4. Verify installation by running `go version` and `go env`.
