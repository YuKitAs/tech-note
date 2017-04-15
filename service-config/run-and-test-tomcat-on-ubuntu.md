# Run And Test Tomcat on Ubuntu

The Tomcat server is started automatically on Ubuntu, to restart or stop Tomcat use the following commands (here we installed Tomcat8):

```console
sudo /etc/init.d/tomcat8 restart
sudo /etc/init.d/tomcat8 stop
```

The default Tomcat admin console can be accessed via the link: `http://localhost:8080/manager/html`. The available users can be defined in the config file `/etc/tomcat/tomcat-users.xml`.

After defined a user and a password, restart the Tomcat server to make the new user activated.
