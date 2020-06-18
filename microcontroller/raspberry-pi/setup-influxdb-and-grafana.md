# Setup InfluxDB and Grafana

## InfluxDB

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

## Grafana

1. Install Grafana (check other versions on the [official website](https://grafana.com/grafana/download/6.3.5?platform=arm)) and start server:

  ```console
  $ wget https://dl.grafana.com/oss/release/grafana_6.3.5_armhf.deb
  $ sudo dpkg -i grafana_6.3.5_armhf.deb

  $ sudo systemctl enable grafana-server
  $ sudo systemctl start grafana-server
  ```

2. Use SSH tunnel to visit Grafana (`localhost:3000` by default) on local machine:

  ```console
  $ ssh -L 3000:localhost:3000 pi@<rpi-ip>
  ```

3. Configure dashboard

  Select datasource `InfluxDB`, HTTP connection URL `localhost:8086`, database `db`, measurement `db_measurement` and field `value`.

  Validate query with `Query Inspector` - there should be no error in the response and the query should look something like this

  ```
  q:"SELECT mean("value") FROM "db" WHERE time >= now() - 1h GROUP BY time(10s) fill(null)"
  ```

  Enable auto-refresh and choose time interval (`Settings -> Time Options`).

## (Optional) Using Python to Interact with InfluxDB

1. Install InfluxDB Python client:

  ```console
  $ pip3 install influxdb
  $ pip3 install --upgrade influxdb
  ```

2. Create Python script:

  ```python
  from influxdb import InfluxDBClient

  json_body = [{
      "measurement": "db_measurement",
      "tags": {
          "author": "YuKitAs"
      },
      "time": "2019-01-01T23:00:00Z",
      "fields": {
          "value": 42
      }
  }]

  client = InfluxDBClient('localhost', 8086)
  client.switch_database('db')
  client.write_points(json_body)
  result = client.query('select value from db_measurement;')
  ```
