import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import structlog
import time

load_dotenv()
from common.logging_config import setup_logging
from .orchestrator import compute_route
from .schemas import RouteRequest, RouteResponse


setup_logging(logfile_path=os.getenv("ROUTING_LOGFILE", "routing.log"))
logger = structlog.get_logger(__name__)

app = FastAPI(title="Routing Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    logger.info("Servicio de enrutamiento iniciado", evento="startup")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        "Petición HTTP entrante",
        metodo=request.method,
        url=str(request.url),
        headers=dict(request.headers)
    )
    start_time = time.time()
    response = await call_next(request)
    elapsed = time.time() - start_time
    logger.info(
        "Petición procesada",
        metodo=request.method,
        url=str(request.url),
        status_code=response.status_code,
        duracion_ms=int(elapsed * 1000)
    )
    return response

@app.post("/route", response_model=RouteResponse)
async def route(req: RouteRequest):
    logger.info(
        "Recibiendo solicitud de ruta",
        inicio=req.start,
        destino=req.end,
        algoritmo=req.algo,
        dirigido=req.directed,
        excluir=req.exclude
    )
    try:
        resultado = await compute_route(req)
        logger.info(
            "Ruta calculada con éxito",
            nodos=resultado.nodes,
            costo=resultado.cost
        )
        return resultado
    except Exception as e:
        logger.error(
            "Error al calcular la ruta",
            error=str(e),
            inicio=req.start,
            destino=req.end,
            algoritmo=req.algo
        )
        raise HTTPException(500, "No se pudo calcular la ruta")
