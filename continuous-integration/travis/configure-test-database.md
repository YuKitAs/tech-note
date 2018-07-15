# Configure Test Database

When using Travis for one of my projects, I need to create a MySQL 5.7 test database for my integration tests.

According to the official docs, I should specify the the following steps in `.travis.yml`:

```yaml
services:
  - mysql
addons: # Install MySQL 5.7
  apt:
    sources:
      - mysql-5.7-trusty # Ubuntu Trusty is `sudo` enabled
    packages:
      - mysql-server
      - mysql-client
before_script: # Configure authentication and create database
  - sudo mysql -e "use mysql; update user set authentication_string=PASSWORD('') where User='root'; update user set plugin='mysql_native_password';FLUSH PRIVILEGES;" # Set `root` user with blank password
  - sudo mysql_upgrade
  - sudo service mysql restart
  - mysql -u root -e "CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';" # Set `username` and `password` according to the project configuration
  - mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO '<username>'@'localhost';"
  - mysql -e "CREATE DATABASE IF NOT EXISTS <test_database_name>;"
```
