# Configuración de watchers en sentinl

Sentinl permite enviar correos electronicos en los cuales se pueden incluir datos de los eventos que se consultan con el Query y que además cumplieron cierta condición.

## Entradas de watcher

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Input
### Condition
### Action


``` html

<h1 style="color:#c00000;font-family:calibri;font-size:28px;text-align:center;">Anomalía Detectada</h1><pre style="color:#21356a;font-family::calibri;font-size:14px">Se tuvo un total de {{payload.hits.total}} eventos, esto prodría indicar que se esta generando un ataque.

<b style="color:#21356a;font-family:calibri;font-size:18px%">Detalles:</b>

 payload.hits.object: {{payload.hits.object}}

<b style="color:#21356a;font-family:calibri;font-size:14px">
Nombre</b>
<div style="color:gray;font-family:calibri;font-size:11px">Área propia
<b>Área de la que depende</b><hr><pre style="color:gray;font-family:calibri;font-size:9px">
Dirección: 
Código Postal: 
Ciudad – País
</pre>

```

Aquí se puede observar como se queda el correo recibido: 

https://www.w3schools.com/code/tryit.asp?filename=FS33JZY259P1

## Acknowledgments

* Gracias para cualquier persona cuyo código se usó

