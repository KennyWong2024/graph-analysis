from __future__ import annotations
import logging
from datetime import date
from typing import Optional, List
from pydantic import BaseModel, model_validator

log = logging.getLogger(__name__)

class MaintenanceRequest(BaseModel):
    days_ahead: Optional[int] = None
    date: Optional[date] = None

    @model_validator(mode="after")
    def validate_exclusive(cls, values):
        log.debug("Validando solicitud de mantenimiento", extra={
            "days_ahead": values.days_ahead,
            "date": values.date
        })
        if values.days_ahead is not None and values.date is not None:
            log.error("Solicitud inválida: se enviaron 'days_ahead' y 'date' simultáneamente")
            raise ValueError("Debe usar solo uno: 'days_ahead' o 'date'")
        if values.days_ahead is None and values.date is None:
            log.info("No se especificó 'days_ahead' ni 'date'; se asumirá la fecha de hoy")
        return values

class MaintenanceResponse(BaseModel):
    reference_day: date
    target_date: date
    day_index: int
    nodes: List[str]
