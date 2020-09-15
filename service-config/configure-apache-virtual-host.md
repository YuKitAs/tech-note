# Configure Apache Virtual Host

1. In `/etc/apache2/sites-available`, copy `000-default.conf` to a new config file.

2. Modify `ServerName`, `DocumentRoot`, etc.

3. Enable new config:

  ```console
  # a2ensite custom.conf
  ```

4. Disable default config:

  ```console
  # a2dissite 000-default.conf
  ```

5. Restart `apache2`:

  ```console
  # service apache2 restart
  ```
