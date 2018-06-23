# Connect to Localhost

In order to connect to the server, we need to specify a base URL for building a retrofit instance. But if our server is running locally, we can't simply use `localhost` as the base URL. In case we are running the app on the emulator, the URL should be `http://10.0.0.2`, and on a real Android device, we should use the IPv4 address (in format `192.168.x.x`) of the computer. On Ubuntu, this IP address can be found in `Connection information`.

