# Use of Secret Tool

The `secret-tool` is a command-line tool to store and access passwords in the GNOME keyring, while `seahorse` is the integrated GUI for GNOME keyring.

* `secret-tool` has to be installed with:

  ```console
  $ sudo apt install libsecret-tools
  ```

* Store passwords with custom attributes:

  ```console
  $ secret-tool store --label='my-pass' <attribute_key> <attribute_value>
  ```

  The password will be typed in the prompt.

  The label will be displayed as password name in the GUI, the attributes will be shown in the `Details` section of the password and can be used to look up passwords.

  The `attribute_key` must be unique, otherwise the existing password matching the attributes will be updated.

* Look up a password by an attribute:

  ```console
  $ secret-tool lookup <attribute_key> <attribute_value>
  ```

* Reference a secret in the script:

  ```bash
  export $MY_PASS=$(secret-tool lookup <attribute_key> <attribute_value>)
  ```
