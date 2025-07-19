import os
import traceback
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import structlog

load_dotenv()

from common.logging_config import setup_logging

LOG_FILE = os.getenv('INGEST_LOGFILE', 'ingest.log')
setup_logging(logfile_path=LOG_FILE)
logger = structlog.get_logger(__name__)

logger.debug(
    "Environment loaded",
    NEO4J_URI=os.getenv("NEO4J_URI"),
    NEO4J_USER=os.getenv("NEO4J_USER")
)

from .neo4j_client import fetch_graph_edges
from .schemas import GraphEdge

app = FastAPI(title="Ingest Service")

@app.on_event("startup")
def on_startup():
    logger.info("Ingest service started")

@app.get("/export-graph", response_model=list[GraphEdge])
def export_graph():
    logger.info("Received request /export-graph")
    try:
        logger.debug("Calling fetch_graph_edges()")
        edges = fetch_graph_edges()
        logger.debug("Mapping edges to Pydantic models", count=len(edges))
        return [GraphEdge(**edge) for edge in edges]
    except Exception:
        err = traceback.format_exc()
        logger.error("Error fetching graph edges", error=err)
        raise HTTPException(status_code=500, detail="Internal Server Error")
