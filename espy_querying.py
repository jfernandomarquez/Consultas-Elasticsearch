from elasticsearch import Elasticsearch
 
es = Elasticsearch(['10.100.64.229:9200'])
res = es.search(index="test", doc_type="articles", body={"query": {"match": {"content": "fox"}}})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['content']))

#es.create(index="test", doc_type="articles", body={"content": "One more fox"})
