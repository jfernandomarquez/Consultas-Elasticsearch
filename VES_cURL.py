#version de elasticsearch usando cURL
import pycurl
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://192.168.20.1:9200/')
c.setopt(c.WRITEFUNCTION, buffer.write)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a string in some encoding. In Python 2, we can print it without knowing what the encoding is.
#print(body)
body_split=body.split('"')
print 'La verison de Elasticsearch es: ',body_split[17]
#for campos in body_split:
#     print 'El campo ',campos
