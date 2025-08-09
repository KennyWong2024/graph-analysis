from __future__ import annotations
import os
import logging
from dataclasses import dataclass
from datetime import date
from zoneinfo import ZoneInfo

_log = logging.getLogger(__name__)

# Estas variables de entorno las quemo en el código porque no son críticas, puede mejorarse con un .env o preguntarlas por consola
# PAra mantener el ejemplo simplificado se trabaja de esta forma

DEFAULT_D0 = "2025-01-01"
DEFAULT_TZ = "America/Costa_Rica"
DEFAULT_SHIFT = 0
DEFAULT_CYCLE_DAYS = 7
DEFAULT_GROUPS_JSON = "/app/data/groups_map.json"


def _parse_date(value: str, fallback: str) -> date:
    try:
        return date.fromisoformat(value)
    except Exception as exc:
        _log.warning(
            "MAINT_D0 inválido (%s), usando fallback %s. Error: %s",
            value, fallback, exc
        )
        return date.fromisoformat(fallback)


def _load_tz(name: str, fallback: str) -> ZoneInfo:
    try:
        return ZoneInfo(name)
    except Exception as exc:
        _log.warning(
            "Zona horaria inválida (%s), usando fallback %s. Error: %s",
            name, fallback, exc
        )
        return ZoneInfo(fallback)


@dataclass(frozen=True, slots=True)
class Settings:
    D0: date
    SHIFT: int
    CYCLE_DAYS: int
    TZ_NAME: str
    TZ: ZoneInfo
    GROUPS_JSON: str


def build_settings() -> Settings:
    d0_env = os.getenv("MAINT_D0", DEFAULT_D0)
    d0 = _parse_date(d0_env, DEFAULT_D0)

    try:
        raw_shift = int(os.getenv("MAINT_SHIFT", str(DEFAULT_SHIFT)))
    except ValueError:
        _log.warning("MAINT_SHIFT inválido, usando %d", DEFAULT_SHIFT)
        raw_shift = DEFAULT_SHIFT

    try:
        cycle_days = int(os.getenv("MAINT_CYCLE_DAYS", str(DEFAULT_CYCLE_DAYS)))
        if cycle_days <= 0:
            raise ValueError("CYCLE_DAYS debe ser > 0")
    except Exception as exc:
        _log.warning(
            "MAINT_CYCLE_DAYS inválido, usando %d. Error: %s",
            DEFAULT_CYCLE_DAYS, exc
        )
        cycle_days = DEFAULT_CYCLE_DAYS

    shift = raw_shift % cycle_days

    tz_name = os.getenv("MAINT_TZ", DEFAULT_TZ)
    tz = _load_tz(tz_name, DEFAULT_TZ)

    groups_json = os.getenv("GROUPS_JSON", DEFAULT_GROUPS_JSON)

    return Settings(
        D0=d0,
        SHIFT=shift,
        CYCLE_DAYS=cycle_days,
        TZ_NAME=tz_name,
        TZ=tz,
        GROUPS_JSON=groups_json
    )

settings = build_settings()