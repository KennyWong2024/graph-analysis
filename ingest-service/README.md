# Conector a Base de Datos
## Descripción General
Microservicio con la única responsabilidad de conectarse mediante *driver Bolt* de **Neo4J** para obtener los datos del grafo a analizar.

## Funcionamiento
El módulo se autentica en la base de datos, esto mediante el usuario y contraseña especificados en las variables de entorno, es importante asegurarse que sean los mismos que en la base de datos. El método utilizado es *Bolt Protocol*, el cuál está optimizado para una comunicación eficiente de consultas con la base de datos.

Evencualmente, una vez autenticado, nuestro cliente realiza una consulta a la base de datos, esto mediante el lenguaje de consulta cypher. La misma luce así: 
```cypher
MATCH (n)-[r:CONECTADO]->(m)
RETURN n.id AS source, m.id AS target, r.distancia AS weight
```
*Nota: Esta fue nuestra consulta inicial experimental, en el codigo final puede diferir por modificaciones u optimizaciones derivados de los descubrimientos en la investigación*

Una vez realizada la consulta necesaria, el microservicio levanta un servidor en *Fast  API* que disponibiliza un **Endpoint (GET)** llamado **/export-graph**, el mismo nos permite obtener el grafo para eventualmente analizarlo con nuestros algoritmos.

Su única dependencia es la base de datos, no consume de ningun otro *Endpoint* sin embargo, es necesario para que **routing-service** obtenga los datos que necesita para la ejecución de los algoritmos.
