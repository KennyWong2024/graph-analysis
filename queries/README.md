# Generación de Datos Neo4j (Docker)

El siguiente paso es para poblar nuestra base de datos en Docker. Aquí es importante entender que estamos usando Neo4j en Docker, no Neo4j Desktop.

Entre las premisas, podemos ejecutar estos mismos comandos en Neo4j Desktop, sí, y por favor háganlo para que visualicen la interfaz gráfica de la base de datos. Sin embargo, que ejecuten estas consultas no implica que vayan a ejecutarse en la base dentro de Docker.

## Escenario

Supongamos que tenemos puntos de venta que debemos estar suministrando, estos puntos son los destinos de entrega, el punto de partida puede ser M (Puntarenas), V (Limón) o el centro de distribución A (San José), la idea es ejecutar algoritmos que nos permitan explorar las formas mas eficientes de distribuir los recursos, para ello, constuiremos una base de datos en Ne4j con datos ficticios que nos permitan realizar el ejercicio.

## Ejecución de Consultas

Para representar este escenario ejecutaremos en orden las siguientes consultas en Cypher:

1. **01-nodos-ciudades.cypher**  
   Ciudades donde tenemos una sede. 

2. **02-aristas-rutas.cypher**  
   Rutas entre distintas ciudades con su respectivo kiloemtraje


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
  -f /queries/01-nodos-ciudades.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/02-aristas-rutas.cypher
```

## Verificación

Para verificar que los datos se cargaron correctamente, puedes ejecutar:

```bash
# Verificar nodos creados
docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  MATCH (a:Location)-[r:CONNECTED]-(b:Location)
  WHERE a.id < b.id
  RETURN 
    a.id   AS Nodo1,
    b.id   AS Nodo2,
    r.distance AS Distancia
  ORDER BY Nodo1, Nodo2;
```

## Reconstrucción con otros datos

#### Limpiar contenedores
Podemos borrar todos los datos y levantar nuevamente la base de datos limpia de forma sencilla con los siguientes comandos:
```bash
# Frenamos las bases y las eliminamos
docker ps -a | grep neo4j | awk '{print $1}' | xargs -r docker stop
docker ps -a | grep neo4j | awk '{print $1}' | xargs -r docker rm

# Borramos la imagen de Neo para trabajar con entornos limpios
docker images | grep neo4j | awk '{print $3}' | xargs -r docker rmi

# Verificamos que no quede nada
docker images | grep neo4j

# Borrar carpetas persistentes (Si da error en Linux Sudo Su)
rm -rf ~/neo4j-data
rm -rf /home/kenny/neo4j-data                                             # <-- Tienen que cambiar y colocar su usuario aquí 
rm -rf /mnt/c/Users/kenny/neo4j-data                                      # <-- Tienen que cambiar y colocar su usuario aquí 
rm -rf /mnt/c/Users/kenny/Documents/Projects/graph-analysis/neo4j-data    # <-- Tienen que cambiar y colocar su usuario aquí 
```

Esta serie de pasos nos garantiza tener un entorno limpio para poder utilizar los datos de nuestra preferencia para realizar pruebas. Nuevamente tenemos que crear la base de datos y eventualmente podriamos modificar la información que hay dentro de las consultas *cyper* y cargar los datos según necesitemos.

#### Levantar base nuevamente:
```bash
# Ir a la raíz del proyecto
cd graph-analysis

# Normalizamos el .env para Unix
dos2unix .env

# Crea un repositorio persistente de los datos
mkdir -p ~/neo4j-data

# Cargue su .env en el terminal
set -o allexport
source .env
set +o allexport

# Verificar variable de entorno 
echo "Password en shell: [$NEO4J_PASSWORD]"

# Levanta la instancia de neo4j
docker run -d --name neo4j-wsl \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH="neo4j/$NEO4J_PASSWORD" \
  -v ~/neo4j-data:/data \
  neo4j:5.9
```

#### Agregar datos a la base:
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
  -f /queries/01-nodos-ciudades.cypher

docker exec neo4j-wsl cypher-shell -u neo4j -p $NEO4J_PASSWORD \
  -f /queries/02-aristas-rutas.cypher
```