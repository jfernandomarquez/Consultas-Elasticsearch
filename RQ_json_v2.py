import requests
import json


print "###################################  SUBO  ###############################################"
print '\n'

r = requests.post('http://192.168.20.1:9200/blog/user/json/', json={"content": "CONTENIDO"})

print r.text


print "\n"
print "#################################  CONSULTO  ##############################################"
print "\n"

response = requests.get('http://192.168.20.1:9200/blog/user/json/') ###### Funciona #####
print response.text

print "\n"
print "################################  SEARCH  ################################################"
print "\n"

response2= requests.post('http://192.168.20.1:9200/blog/_search?pretty=true', json={'query': {'match': { 'content': 'CONTENIDO'}}})
print response2.text
