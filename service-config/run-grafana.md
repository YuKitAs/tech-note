# Run Grafana

After downloading and installing Grafana from the [official site](https://grafana.com/grafana/download/5.2.0-beta1?platform=arm), start the server with:

```console
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

Visit `localhost:3000`, the default username and password are both `admin`.
