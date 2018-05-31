# Este algoritmo hace una consulta de todos los asa y lista los ciudades de estados unidos de donde se tiene acceso

import requests
import json

r= requests.post('http://192.168.20.1:9200/asa-*/_search?pretty=true', json={"size":100,"query":{"bool":{"must":{"match":{"geoip.country_name":"United"}}}}})

a=r.text.split('"')

city_name=[]

for i in range(0,len(a)):
	if a[i] == 'city_name':
		city_name.append(a[i+2])
		
print "\nLos ciudades de USA donde se han tenido conexiones por VPN de vinculados son:\n "
for j in range(len(city_name)):
	print j+1, city_name[j]
print "\n"


