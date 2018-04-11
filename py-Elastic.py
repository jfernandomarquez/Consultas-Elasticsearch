from elasticsearch import Elasticsearch

es = Elasticsearch(['192.168.1.58:9200']) #esclient
#es=Elasticsearch([{'host': 'localhost', 'port': 9200}])
r=es.search()
print r
print "-----------------"
print es.info()

