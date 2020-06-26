# Change Username of the Current User

Theoretically, when there is only one user logged in, it's not possible to change the username of the current user. One stupid but quick solution is to use a temporary user with `sudo` rights to do it. So generally follow these steps (on Ubuntu):

1. Create a temporary user named whatever like `temp` and set password:

  ```console
  $ sudo adduser temp
  $ sudo passwd temp
  ```

2. Add him into `sudo` group:

  ```console
  $ sudo adduser temp sudo
  ```

3. Log out and log in with `temp`.

4. Change the username as we want and change the name of the `home` folder:

  ```console
  $ sudo usermod -l <new-name> -d /home/<new-name> -m <old-name>
  ```

  For safety, we could use `grep -IRFl /home/<old-name> ~` to list all the references to the old `home`.

5. Log out `temp` and log in back again with the actual user.

6. Delete the temporary user and remove his `home`:

  ```console
  $ sudo deluser temp
  $ sudo rm -rf /home/temp
  ```
