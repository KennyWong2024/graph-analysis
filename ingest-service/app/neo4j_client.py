import os
import traceback
from neo4j import GraphDatabase
import structlog

logger = structlog.get_logger(__name__)

NEO4J_URI      = os.getenv("NEO4J_URI")
NEO4J_USER     = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

logger.debug(
    "Neo4j config",
    uri=NEO4J_URI,
    user=NEO4J_USER
)

try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    logger.info("Neo4j driver initialized")
except Exception:
    err = traceback.format_exc()
    logger.error("Failed to initialize Neo4j driver", error=err)
    raise

def fetch_graph_edges():
    logger.info("Starting fetch_graph_edges")
    query = """
    MATCH (n)-[r:CONECTADO]->(m)
    RETURN n.id AS source, m.id AS target, r.distancia AS weight
    """
    edges = []
    try:
        with driver.session() as session:
            logger.debug("Executing Cypher query", query=query.strip())
            result = session.run(query)
            for record in result:
                s = record["source"]
                t = record["target"]
                w = record["weight"]
                logger.debug("Fetched edge", source=s, target=t, weight=w)
                edges.append({"source": s, "target": t, "weight": w})
        logger.info("Completed fetch_graph_edges", count=len(edges))
        return edges

    except Exception:
        err = traceback.format_exc()
        logger.error("Exception in fetch_graph_edges", error=err)
        raise
