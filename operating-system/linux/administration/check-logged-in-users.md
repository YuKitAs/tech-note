# Check Logged-in Users

* Get usernames who are currently logged in the current host:

  ```console
  $ users
  ```

* Get a summary of logged-in users (from `/var/run/utmp` and `/var/log/wtmp`):

  ```console
  $ who
  ```

  The result contains username, tty number, login datetime and machine address.

* Get logged-in users with extensive information (from `/var/run/utmp` and `/proc`):

  ```console
  $ w
  ```

* Get login history of all users or a specific user:

  ```console
  $ last [username]
  ```
