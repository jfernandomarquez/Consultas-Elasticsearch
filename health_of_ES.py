from elasticsearch import Elasticsearch

es=Elasticsearch(['x.x.x.x:x'])

r=es.cluster.health()

print r[u'status']
