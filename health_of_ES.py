# Saber el estado de ElasticSearch (Green,Yellow,Red)

from elasticsearch import Elasticsearch

es=Elasticsearch(['192.168.20.1:9200'])

r=es.cluster.health()

print r[u'status']
