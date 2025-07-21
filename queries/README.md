# Generación de Datos Neo4j (Docker)

El siguiente paso es para poblar nuestra base de datos en Docker. Aquí es importante entender que estamos usando Neo4j en Docker, no Neo4j Desktop.

Entre las premisas, podemos ejecutar estos mismos comandos en Neo4j Desktop, sí, y por favor háganlo para que visualicen la interfaz gráfica de la base de datos. Sin embargo, que ejecuten estas consultas no implica que vayan a ejecutarse en la base dentro de Docker.

## Escenario

La justificación del laboratorio y lo que se busca recrear con datos ficticios es lo siguiente:

En el escenario planteado tenemos un centro de distribución de compras en línea. Los artículos a entregar habitualmente son pequeños y cada mañana recibimos una base de datos con las entregas del día, previamente confirmadas con el cliente la disponibilidad.

Nuestro trabajo es recopilar la dirección en la que el cliente desea recibir su artículo, procesar el dato e incluirlo en la base.

El algoritmo debe encontrar la ruta más óptima de entrega, incluir el pedido y dar al cliente distintas opciones disponibles para entrega, calculando las rutas con base en la distancia.

Para representar el ejercicio utilizaremos las siguientes coordenadas de clientes, nuestro CEDI y los cruces:
*[Aquí falta completar la información sobre las coordenadas]*

## Ejecución de Consultas

Para representar este escenario ejecutaremos en orden las siguientes consultas en Cypher:

1. **01-nodos-clientes.cypher**  
   Crea los nodos `Cliente` A–H.  

2. **02-nodos-cruces.cypher**  
   Crea los nodos `Cruce` I–Z.  

3. **03-conexiones-bidireccionales.cypher**  
   Crea las relaciones `:CONECTADO` en ambas direcciones con sus distancias.

## Comandos de Ejecución

Asumiendo que tu contenedor de Neo4j en Docker se llama `neo4j-wsl`:

Primero no olvidemos levantar la base de datos. Abrimos Docker, luego abrimos un terminal en WSL e iniciamos la base:

```bash
# Levantar Base
docker start neo4j-wsl
```

Ejecutamos las consultas:

```bash
# Ir a la raíz del proyecto
cd graph-analysis

# Cargar su .env en el terminal
set -o allexport
source .env
set +o allexport

# Verificar variable de entorno 
echo "Password en shell: [$NEO4J_PASSWORD]"

# Copiar las consultas al contenedor
docker cp queries neo4j-wsl:/queries

# Ejecutar consultas en orden
docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/01-nodos-clientes.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/02-nodos-cruces.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/03-conexiones-bidireccionales.cypher
```

## Verificación

Para verificar que los datos se cargaron correctamente, puedes ejecutar:

```bash
# Verificar nodos creados
docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -c "MATCH (n) RETURN labels(n), count(n)"
```