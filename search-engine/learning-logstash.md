# Learning Logstash

Current version: 6.2.2

Table of Contents

* [Introduction](#introduction)
  * [Logstash](#logstash)
  * [Beats](#beats)
* [Configuring Logstash and Filebeat](#configuring-logstash-and-filebeat)
* [Using Filter Plugins](#using-filter-plugins)
* [Indexing Data into Elasticsearch](#indexing-data-into-elasticsearch)

## Introduction
### Logstash
[Logstash](https://www.elastic.co/products/logstash) is a server-side data processing pipeline, which can ingest data from multiple disparate sources, parse it and write it to an Elasticsearch cluster (or other stash). Logstash is a part of the ELK Stack.

Download Logstash from [here](https://www.elastic.co/downloads/logstash). I encountered an issue "Unable to find JRuby." with the `zip` because the `vendor/jruby` directory is missing, it's better to download the `tar.gz`.

A Logstash pipeline consists of two required elements `input` and `output`, and one optional element `filter`.

### Beats

Beats are introduced into ELK as a family of lightweight, single-purpose agents for shipping logs or metrics.

Among them, [Filebeat](https://www.elastic.co/products/beats/filebeat) is a real-time log data shipper for local files. Logstash is usually used together with Filebeat when logging files.

> Filebeat monitors the log directories or specific log files, tails the files, and forwards them either to Elasticsearch or Logstash for indexing.

In this example, Logstash pipeline uses Filebeat to read a log file and writes the parsed data to Elasticsearch.

Download Filebeat from [here](https://www.elastic.co/downloads/beats/filebeat).

## Configuring Logstash and Filebeat

First, we need to configure Filebeat. In `filebeat.yml`, edit absolute path to the log file, uncomment `output.logstash` and `hosts ["localhost:5044"]`.

In the command line, start Filebeat by running:

```console
$ ./filebeat -e -c filebeat.yml -d "publish"
```

Then we configure Logstash by creating a configuration pipeline (eg. `logstash.conf`) in the home directory of Logstash, the layout is like:

```
input {
}
# filter {
# This section is optional.
# }
output {
}
```

In the `input` section, if we are using Beats, we can add the following lines:

```
beats {
    port => "5044"
}
```

Otherwise, we can use `stdin {}` or specify path to the log file.

In the `output` section, we can either print to console using `stdout { codec => rubydebug }` or write to Elasticsearch.

Run the following command to test the configuration:

```console
$ ./bin/logstash -f logstash.conf --config.test_and_exit
```

On success we should see "Config Validation Result: OK", then run the following command to start Logstash:

```console
$ ./bin/logstash -f logstash.conf --config.reload.automatic
```

The last argument means Logstash will restart automatically whenever the configuration file is modified.

## Using Filter Plugins

Filter plugins are used to filter log data, they should be configured in the `filter` section of the configuration file.

One of the most useful plugins is [Grok](https://www.elastic.co/guide/en/logstash/6.2/plugins-filters-grok.html). It's avaliable by default in Logstash and can help to parse and structure text using regular expressions or custom patterns. When using Grok, the `filter` section may look like:

```
filter {
    grok {
        match => { "message" => "%{COMBINEDAPACHELOG}" }
    }
}
```
The `%{COMBINEDAPACHELOG}` pattern structures Apache log lines using a specific schema with fields `clientip`, `ident`, `auth` and so on.

Elastic filter plugins are listed [here](https://www.elastic.co/guide/en/logstash/6.2/filter-plugins.html).

After configured filter plugin, we need to shutdown Filebeat, delete the `data/registry` file and restart it.

## Indexing Data into Elasticsearch

To index the data into an Elasticsearch cluster, we could configure the `output` section in `logstash.conf` as follows to create a new index `logstash_test`:

```
output {
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "logstash_test"
    }
}
```
