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

```bash
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

`num = int(input('Introduzca un numero: '))`


[![blogger](http://icons.iconarchive.com/icons/carlosjj/google-jfk/128/blogger-icon.png)](https://jfernandomarquez.blogspot.com/) 
