from __future__ import annotations
import logging
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Optional

log = logging.getLogger(__name__)

def _today_in_tz(tz: ZoneInfo) -> date:
    return datetime.now(tz).date()

def _mod(n: int, m: int) -> int:
    return (n % m + m) % m

def resolve_target_date(
    days_ahead: Optional[int],
    date_str: Optional[date],
    tz: ZoneInfo
) -> date:
    if date_str is not None:
        log.info("Se recibió 'date' explícita", extra={"date": str(date_str)})
        return date_str
    today = _today_in_tz(tz)
    if days_ahead is not None:
        target = today + timedelta(days=days_ahead)
        log.info(
            "Se calculará fecha objetivo sumando días a partir de hoy",
            extra={"today": str(today), "days_ahead": days_ahead, "target_date": str(target)}
        )
        return target
    log.info("No se recibieron parámetros; se usará la fecha de hoy", extra={"today": str(today)})
    return today

def compute_day_index(
    target_date: date,
    d0: date,
    cycle_days: int,
    shift: int = 0
) -> int:
    days_diff = (target_date - d0).days
    base_index = _mod(days_diff, cycle_days)
    effective_index = _mod(base_index + shift, cycle_days)
    log.debug(
        "Cálculo de índice de mantenimiento",
        extra={
            "target_date": str(target_date),
            "d0": str(d0),
            "cycle_days": cycle_days,
            "days_diff": days_diff,
            "base_index": base_index,
            "shift": shift,
            "effective_index": effective_index
        }
    )
    return effective_index