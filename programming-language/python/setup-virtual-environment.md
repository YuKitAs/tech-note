# Setup Virtual Environment

[Virtualenv](https://virtualenv.pypa.io/en/stable/) is a tool to create isolated python environment.

Installation and usage:

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

4. In the project root directory, use the following command to activate the virtual environment:

  ```console
  $ . env/bin/activate
  ```

  The name of the current virtual environment will appear on the left like:

  ```console
  (env) yukitas@computer:path/to/project$
  ```

5. In the virtual environment, check if the python3 interpreter is successfully set:

  ```console
  $ python --version
  ```

  It should be `Python 3.*` when outside the environment it's `Python 2.7.*` with the same command.

6. To leave the virtual environment, run:

  ```console
  $ deactivate
  ```
