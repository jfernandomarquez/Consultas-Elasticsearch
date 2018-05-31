import requests
r = requests.get('http://192.168.20.1:9200/')
cont=r.content
a=cont=cont.split('"')
print a[1], ":" , a[3]
print a[5],":" , a[7]
print a[13],":", a[17]
