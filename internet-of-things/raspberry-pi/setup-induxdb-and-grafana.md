# Setup InduxDB and Grafana

1. Install InduxDB and start server:

  ```console
  $ curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
  $ echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
  $ sudo apt update
  $ sudo apt install influxdb  

  $ sudo systemctl enable influxdb
  $ sudo systemctl start influxdb

  $ influx
  ```

2. Create database and measurement:

  ```console
  CREATE DATABASE db
  USE db
  INSERT db_measurement,author=YuKitAs value=42
  ```

3. Install Grafana (check other versions on the [official website](https://grafana.com/grafana/download/6.3.5?platform=arm)) and start server:

  ```console
  $ wget https://dl.grafana.com/oss/release/grafana_6.3.5_armhf.deb
  $ sudo dpkg -i grafana_6.3.5_armhf.deb

  $ sudo systemctl enable grafana-server
  $ sudo systemctl start grafana-server
  ```

4. Use SSH tunnel to visit Grafana (`localhost:3000` by default) on local machine:

  ```console
  $ ssh -L 3000:localhost:3000 pi@<rpi-ip>
  ```

4. Configure dashboard

  Select datasource `InfluxDB`, HTTP connection URL `localhost:8086`, database `db`, measurement `db_measurement` and field `value`.

  Validate query with `Query Inspector` - there should be no error in the response and the query should look something like this

  ```
  q:"SELECT mean("value") FROM "db" WHERE time >= now() - 1h GROUP BY time(10s) fill(null)"
  ```
