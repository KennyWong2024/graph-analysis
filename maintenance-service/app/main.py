from __future__ import annotations
import logging
from datetime import date as DateType
from fastapi import FastAPI, Query, HTTPException
from .schemas import MaintenanceResponse
from .orchestrator import get_maintenance

log = logging.getLogger(__name__)
app = FastAPI(title="maintenance-service")

@app.on_event("startup")
async def on_startup():
    log.info("Servicio de mantenimiento iniciado")

@app.get("/maintenance", response_model=MaintenanceResponse)
def maintenance_get(
    days_ahead: int | None = Query(default=None),
    date: DateType | None = Query(default=None) 
):
    if days_ahead is not None and date is not None:
        log.error("Solicitud inválida: se enviaron 'days_ahead' y 'date' simultáneamente")
        raise HTTPException(status_code=400, detail="Debe usar solo uno: 'days_ahead' o 'date'")
    resp = get_maintenance(days_ahead=days_ahead, date_str=date)
    log.info("Consulta GET procesada", extra={"day_index": resp.day_index, "target_date": str(resp.target_date)})
    return resp
