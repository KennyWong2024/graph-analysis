from __future__ import annotations
import logging
from datetime import date
from typing import Optional
from .config import settings
from .schemas import MaintenanceResponse
from .services.calendar_service import resolve_target_date, compute_day_index
from .services.loader import get_nodes_for_index

log = logging.getLogger(__name__)

def get_maintenance(days_ahead: Optional[int], date_str: Optional[date]) -> MaintenanceResponse:
    log.info("Iniciando orquestación de consulta de mantenimiento", extra={
        "param_days_ahead": days_ahead,
        "param_date": str(date_str) if date_str else None,
        "reference_day": str(settings.D0),
        "timezone": settings.TZ_NAME,
        "cycle_days": settings.CYCLE_DAYS,
        "shift": settings.SHIFT
    })

    target_date = resolve_target_date(days_ahead=days_ahead, date_str=date_str, tz=settings.TZ)
    day_index = compute_day_index(
        target_date=target_date,
        d0=settings.D0,
        cycle_days=settings.CYCLE_DAYS,
        shift=settings.SHIFT
    )
    nodes = get_nodes_for_index(day_index)

    log.info("Orquestación completada", extra={
        "target_date": str(target_date),
        "day_index": day_index,
        "n_nodes": len(nodes)
    })

    return MaintenanceResponse(
        reference_day=settings.D0,
        target_date=target_date,
        day_index=day_index,
        nodes=nodes
    )
