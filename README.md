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
input {
  jdbc {
    type => "smnet"
    jdbc_validate_connection => true
    jdbc_driver_library => "/opt/logstash/drivers/postgresql-42.2.2.jar"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_connection_string => "jdbc:postgresql://10.100.67.50:5432/smnet"
    jdbc_user => "elkddl042318"
    jdbc_password => "elk456"
    statement => "SELECT * from audit_log WHERE n_id > :sql_last_value"
    use_column_value => true
    tracking_column => "n_id"
    tracking_column_type => "numeric"
#    sequel_opts => {login_timeout => 5 }
    jdbc_paging_enabled => true
    jdbc_page_size => 2000
    schedule => "*/5 * * * *"
#    record_last_run => true
#    last_run_metadata_path => "/opt/logstash/logstash_jdbc_last_run.txt"
#    clean_run => true 
  }
}
```


```python
input {
  jdbc {
    type => "smnet"
    jdbc_validate_connection => true
    jdbc_driver_library => "/opt/logstash/drivers/postgresql-42.2.2.jar"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_connection_string => "jdbc:postgresql://10.100.67.50:5432/smnet"
    jdbc_user => "elkddl042318"
    jdbc_password => "elk456"
    statement => "SELECT * from audit_log WHERE n_id > :sql_last_value"
    use_column_value => true
    tracking_column => "n_id"
    tracking_column_type => "numeric"
#    sequel_opts => {login_timeout => 5 }
    jdbc_paging_enabled => true
    jdbc_page_size => 2000
    schedule => "*/5 * * * *"
#    record_last_run => true
#    last_run_metadata_path => "/opt/logstash/logstash_jdbc_last_run.txt"
#    clean_run => true 
  }
}
```

```bash
input {
  jdbc {
    type => "smnet"
    jdbc_validate_connection => true
    jdbc_driver_library => "/opt/logstash/drivers/postgresql-42.2.2.jar"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_connection_string => "jdbc:postgresql://10.100.67.50:5432/smnet"
    jdbc_user => "elkddl042318"
    jdbc_password => "elk456"
    statement => "SELECT * from audit_log WHERE n_id > :sql_last_value"
    use_column_value => true
    tracking_column => "n_id"
    tracking_column_type => "numeric"
#    sequel_opts => {login_timeout => 5 }
    jdbc_paging_enabled => true
    jdbc_page_size => 2000
    schedule => "*/5 * * * *"
#    record_last_run => true
#    last_run_metadata_path => "/opt/logstash/logstash_jdbc_last_run.txt"
#    clean_run => true 
  }
}
```

`num = int(input('Introduzca un numero: '))`


[![blogger](http://icons.iconarchive.com/icons/carlosjj/google-jfk/128/blogger-icon.png)](https://jfernandomarquez.blogspot.com/) 
