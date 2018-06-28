# ELK-Scripts
Scripts para consultar los logs almacenados en ElasticSearch

Inicialmente se exploran diversas maneras de realizar Querie, utilizando:

* python
* bash
* curl
* elasticsearch-py

La idea es poder encontrar eventos extraños en los logs.

<details>
<summary>"Click to expand"</summary>
this is hidden
</details>



<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

I think you should use an
`<addr>` element here instead.

def foo():
    if not bar:
        return True
        
        
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column


```javascript
GET /logstash-*/_search?filter_path=hits.total
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "task": "logon"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-5m/m",
              "lt": "now"
            }
          }
        }
      ]
    }
  }
}
```


```python
import datetime
import time


def tiempo():
        st = datetime.datetime.fromtimestamp(time.time())
        Y= st.strftime('%Y')
        m= st.strftime('%m')
        d= st.strftime('%d')
        H= st.strftime('%H')
        M= st.strftime('%M')
        return Y,m,d,H,M

Y,m,d,H,M=tiempo()
id_doc=d
f = open("mydata/dataset_real_{0}".format(id_doc)+".txt", "w")
f.write('  Ano  Mes     Dia     Hora    Minutos          Count\n')
f.write(' \n')
f.close()

from elasticsearch import Elasticsearch
es = Elasticsearch(['10.100.64.229:9200'])

while True:
	Y,m,d,H,M=tiempo()
	r = es.search(index="windows-*", filter_path="hits.total", body={"query":{"bool":{"must":[{"match":{"task":"Authentication failure"}},{"range":{"@timestamp":{"gte":"now-5m/m","lt":"now"}}}]}}})
	count=r["hits"]["total"]
	f = open("mydata/dataset_real_{0}".format(id_doc)+".txt", "a")
	f.write('  {}	{}	{}	{}	{}		{}	  {}\n'.format(Y,m,d,H,M,count,"Data"))
	f.close()
	print "Querying..."+ " Hora:" + str(H) + " Minuto:" + str(M) + " dia:" + str(d)
	time.sleep(300)
```

```bash
import datetime
import time
def tiempo():
st = datetime.datetime.fromtimestamp(time.time())
Y= st.strftime('%Y')
m= st.strftime('%m')
d= st.strftime('%d')
H= st.strftime('%H')
M= st.strftime('%M')
return Y,m,d,H,M
Y,m,d,H,M=tiempo()
id_doc=d
f = open("mydata/dataset_real_{0}".format(id_doc)+".txt", "w")
f.write(' Ano Mes Dia Hora Minutos Count\n')
f.write(' \n')
f.close()
from elasticsearch import Elasticsearch
es = Elasticsearch(['10.100.64.229:9200'])
while True:
Y,m,d,H,M=tiempo()
r = es.search(index="windows-*", filter_path="hits.total", body={"query":{"bool":{"must":
[{"match":{"task":"Authentication failure"}},{"range":{"@timestamp":{"gte":"now-5m/m","lt":"n
ow"}}}]}}})
count=r["hits"]["total"]
f = open("mydata/dataset_real_{0}".format(id_doc)+".txt", "a")
f.write(' {} {} {} {} {} {} {}\n'.format(Y,m,d,H,M,count,"Data"))
f.close()
print "Querying..."+ " Hora:" + str(H) + " Minuto:" + str(M) + " dia:" + str(d)
time.sleep(300)
```

`num = int(input('Introduzca un numero: '))`


[![blogger](http://icons.iconarchive.com/icons/carlosjj/google-jfk/128/blogger-icon.png)](https://jfernandomarquez.blogspot.com/) 
