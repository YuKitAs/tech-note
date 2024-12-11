# Use Aliases in Bash Scripts

The aliases defined in `.bash_aliases` or `.bashrc` can't be used in Bash scripts since they are only for interactive shells. There are two workarounds.

1. Enable Alias Expansion

  Add `shopt -s expand_aliases` before using aliases in the script:

  ```bash
  #!/bin/bash
  shopt -s expand_aliases
  alias docker-compose='docker compose'
  ```

  or if the alias is defined in `./bash_aliases`:

  ```bash
  #!/bin/bash
  shopt -s expand_aliases
  source ~/.bash_aliases
  ```

2. Define functions instead of aliases

  In `.bashrc`:

  ```bash
  docker-compose() {
    docker compose "$@"
  }
  ```

  Then export the function:

  ```console
  $ . ~/.bashrc
  $ export -f docker-compose
  ```

  The definitions of exported functions can be found with

  ```console
  $ declare -fx
  ```

  Unset the function with

  ```console
  $ unset -f docker-compose
  ```
