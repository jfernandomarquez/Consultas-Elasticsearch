import requests
import json

print "\n"
print "#################################  CONSULTO  ##############################################"
print "\n"

response = requests.get('http://192.168.1.60:9200/logstash-*/log/_search', json={"size":1,"query":{"match_all":{}}})) 
print response.text
