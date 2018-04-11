#!/bin/bash

curl -H 'Content-Type: application/x-ndjson' -XPOST 'http://192.168.1.58:9200/bank/account/_bulk?pretty' --data-binary @accounts.json
curl -H 'Content-Type: application/x-ndjson' -XPOST 'http://192.168.1.58:9200/shakespeare/doc/_bulk?pretty' --data-binary @shakespeare_6.0.json
curl -H 'Content-Type: application/x-ndjson' -XPOST 'http://192.168.1.58:9200/_bulk?pretty' --data-binary @logs.jsonl
