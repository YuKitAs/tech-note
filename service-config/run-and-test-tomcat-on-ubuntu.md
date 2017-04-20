# Run And Test Tomcat on Ubuntu

The Tomcat server is started automatically on Ubuntu, to restart or stop Tomcat use the following commands:

```console
sudo /etc/init.d/tomcat{X} restart
sudo /etc/init.d/tomcat{X} stop
```

`{X}` is the Tomcat major version number.

The default Tomcat admin console can be accessed via the link: `http://localhost:8080/manager/html`. The available users can be defined in the config file `/etc/tomcat/tomcat-users.xml`.

After defined a user and a password, restart the Tomcat server to make the new user activated.

Directories for Tomcat:

* `/etc/tomcat{X}`: for configuration
* `/usr/share/tomcat{X}`: CATALINA_HOME, for runtime
* `/usr/share/tomcat{X}-root`: for webapps
* `/var/lib/tomcat{X}`: CATALINA_BASE, alternative path to Tomcat
