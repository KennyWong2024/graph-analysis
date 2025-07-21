import os
import traceback
from neo4j import GraphDatabase
import structlog

logger = structlog.get_logger(__name__)

NEO4J_URI      = os.getenv("NEO4J_URI")
NEO4J_USER     = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

logger.debug(
    "Configuración de Neo4j",
    uri=NEO4J_URI,
    user=NEO4J_USER
)

try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    logger.info("Driver de Neo4j inicializado")
except Exception:
    err = traceback.format_exc()
    logger.error("Error al inicializar el driver de Neo4j", error=err)
    raise

def fetch_graph_edges():
    logger.info("Iniciando obtención de aristas del grafo")
    query = """
    MATCH (n)-[r:CONECTADO]->(m)
    RETURN n.id AS source, m.id AS target, r.distancia AS weight
    """
    edges = []
    try:
        with driver.session() as session:
            logger.debug("Ejecutando consulta Cypher", query=query.strip())
            result = session.run(query)
            for record in result:
                s = record["source"]
                t = record["target"]
                w = record["weight"]
                logger.debug(
                    "Arista obtenida",
                    source=s,
                    target=t,
                    weight=w
                )
                edges.append({"source": s, "target": t, "weight": w})
        logger.info(
            "Finalizada obtención de aristas",
            cantidad=len(edges)
        )
        return edges

    except Exception:
        err = traceback.format_exc()
        logger.error("Excepción al obtener aristas del grafo", error=err)
        raise
