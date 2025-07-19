# Generación de Datos Neo4J (Docker)
El siguiente paso es para poblar nuestra base de datos en Docker, aquí es importante entender, estamos usando Neo4J en Docker, no Neo4J Desktop.

Entre las premisas, podemso ejecutar estos mismos comandos en Neo4J Desktop, si, y por favor haganlo para que visualicen la interfas gráfica de la base de datos, sin embargo el que ejecuten estas consultas no implican que vana  ejecutarse en la base dentro de Docker.

## Escenario
La justifcación del laboratorio y lo que se busca recrear con datos ficticios es lo siguiente:
* 
En el escenario planteado tenemos un centro de distribución de compras en línea, los artículos a entregar habitualmente son pequeños y cada mañana recibimos una base de datos con las entregas del día, previamente ya confirmado con el cliente la disponibilidad.

Nuestro trabajo es recopilar la dirección en la que el cliente desea recibir su artículo, procesar el dato e incluirlo en la base.

El algoritmo debe encontrar la ruta mas optima de entrega, incluir el pedido y dar al cliente distintas opciones disponibles para entrega, calculando las rutas con base a distancia.

Para representar el ejercicio utilizaremos las siguientes coordinadas de clientes, nuestro CEDI y los cruces. 
*

Para representar este escenario ejecutaremso en orden las siguientes consultas en Cypher:
1. **01-nodos-clientes.cypher**  
   Crea los nodos `Cliente` A–H.  
2. **02-nodos-cruces.cypher**  
   Crea los nodos `Cruce` I–Z.  
3. **03-conexiones-bidireccionales.cypher**  
   Crea las relaciones `:CONECTADO` en ambas direcciones con sus distancias.

Asumiendo que tu contenedor de Neo4j en Docker se llama `neo4j-wsl`:

Primero no olvidamos levantar la base de datos, abrimos docker, luego abrimos un terminal en WSL e iniciamos la base:

```bash
# Levantar Base
docker start neo4j-wsl
```

Ejecutamos las consultas:
```bash
# Ir a la raiz dle proyecto
cd graph-analysis

# Cargue su .env en el terminal
set -o allexport
source .env
set +o allexport

# Verificar variable de entorno 
echo "Password en shell: [$NEO4J_PASSWORD]"

# Copia las consultas al contenedor
docker cp queries neo4j-wsl:/queries

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/01-nodos-clientes.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/02-nodos-cruces.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/03-conexiones-bidireccionales.cypher
```