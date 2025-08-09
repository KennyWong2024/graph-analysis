from __future__ import annotations
import logging
import json
from pathlib import Path
from typing import List, Dict
from ..config import settings

log = logging.getLogger(__name__)

_groups_cache: Dict[str, List[str]] | None = None

def _load_groups_once() -> Dict[str, List[str]]:
    global _groups_cache
    if _groups_cache is None:
        path = Path(settings.GROUPS_JSON)
        log.info("Cargando mapa de grupos desde archivo", extra={"path": str(path)})
        with open(path, "r", encoding="utf-8") as f:
            _groups_cache = json.load(f)
        log.debug("Mapa de grupos cargado en memoria", extra={"keys": list(_groups_cache.keys())})
    return _groups_cache

def get_nodes_for_index(day_index: int) -> List[str]:
    log.info("Obteniendo nodos para índice de mantenimiento", extra={"day_index": day_index})
    groups = _load_groups_once()
    nodes = groups.get(str(day_index), [])
    log.debug("Nodos obtenidos para índice", extra={"day_index": day_index, "total": len(nodes)})
    return nodes
