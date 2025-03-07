# Setup Virtual Environment


**Update: Python 3.3+ includes the built-in `venv` module and `virtualenv` doesn't need to be installed manually.**

Activate virtual environment with:

```console
$ . venv/bin/activate
```

## For Older Versions
[Virtualenv](https://virtualenv.pypa.io/en/stable/) is a tool to create isolated python environment.

### Installation

1. Install `virtualenv`:

  ```console
  $ sudo apt install virtualenv
  ```

2. Create a virtual environment for a project:

  ```console
  $ cd /path/to/project
  $ virtualenv env
  ```

  Then a directory called `env` will be created, which should be added into `.gitignore`.

3. If we want to use the python3 interpreter in the virtual environment, we can specify the path like:

  ```console
  $ virtualenv -p $(which python3) env
  ```

### Usage

1. In the project root directory, use the following command to activate the virtual environment:

  ```console
  $ . env/bin/activate
  ```

  The name of the current virtual environment will appear on the left like:

  ```console
  (env) yukitas@computer:path/to/project$
  ```

2. In the virtual environment, check if the python3 interpreter is successfully set:

  ```console
  $ python --version
  ```

  It should be `Python 3.*` when outside the environment it's `Python 2.7.*` with the same command.

3. To leave the virtual environment, run:

  ```console
  $ deactivate
  ```

## Configuration in PyCharm

1. Go to `File -> Settings`, search for `Project Interpreter`.

2. Add a new interpreter by selecting `Existing environment`.
