# Install Apache 2 and PHP 5.6 on Ubuntu 16.04

Check if PHP is in the list of installed package:
```console
dpkg -l | grep php
```

Add PPA:
```console
sudo add-apt-repository ppa:ondrej/php
```

Install Apache 2 and PHP 5.6:
```console
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install php5.6
```

Verify Apache by visiting `localhost` in web browser.

Add helper package so that PHP can run under the Apache server:
```console
sudo apt-get install libapache2-mod-php5
```
