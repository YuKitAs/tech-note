# Dejavu Intro

Unlike Kibana, which uses server-side page-rendering techniques, [Dejavu](https://github.com/appbaseio/dejavu) (built with React v15.6.0) can build a Web UI with client-side rendering. 

Features:

* no page reloads

* infinite scroll

* filtered views

* realtime updates (CRUD)

Dejavu uses a websockets based API and subscribe for data changes for the current filtered view. So the Elasticsearch server needs to support a websockets based publish API. (Recommended API to host data: appbase.io)

Dejavu supports importing/exporting JSON and CSV data directly into Elasticsearch through a guided data mappings configuration (GUI: [importer](https://appbaseio-confidential.github.io/importer/)).
