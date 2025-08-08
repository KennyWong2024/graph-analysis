import os
import traceback
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
import structlog

load_dotenv()

from common.logging_config import setup_logging

LOG_FILE = os.getenv('INGEST_LOGFILE', 'ingest.log')
setup_logging(logfile_path=LOG_FILE)
logger = structlog.get_logger(__name__)

logger.debug(
    "Entorno cargado",
    NEO4J_URI=os.getenv("NEO4J_URI"),
    NEO4J_USER=os.getenv("NEO4J_USER")
)

from .neo4j_client import fetch_graph_edges
from .schemas import GraphEdge

app = FastAPI(title="Ingest Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    logger.info("Servicio de ingestión iniciado")

@app.get("/export-graph", response_model=list[GraphEdge])
def export_graph():
    logger.info("Solicitud recibida en /export-graph")
    try:
        logger.debug("Llamando a fetch_graph_edges()")
        edges = fetch_graph_edges()
        logger.debug("Transformando aristas a modelos Pydantic", cantidad=len(edges))
        return [GraphEdge(**edge) for edge in edges]
    except Exception:
        err = traceback.format_exc()
        logger.error("Error al obtener aristas del grafo", error=err)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
