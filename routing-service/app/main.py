import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import structlog

load_dotenv()
from common.logging_config import setup_logging
from .orchestrator import compute_route
from .schemas import RouteRequest, RouteResponse

setup_logging(logfile_path=os.getenv("ROUTING_LOGFILE", "routing.log"))
logger = structlog.get_logger(__name__)

app = FastAPI(title="Routing Service")

@app.on_event("startup")
def startup():
    logger.info("Routing service started")

@app.post("/route", response_model=RouteResponse)
async def route(req: RouteRequest):
    logger.info("Received route request", start=req.start, end=req.end, algo=req.algo, directed=req.directed)
    try:
        return await compute_route(req)
    except Exception as e:
        logger.error("Routing error", error=str(e))
        raise HTTPException(500, "Could not compute route")
