from pydantic import BaseModel
from typing import List, Optional, Tuple

class NodeAccumulated(BaseModel):
    node: str
    accumulated: float

class RouteRequest(BaseModel):
    start:    str
    end:      Optional[str] = None
    algo:     str
    directed: bool = False
    exclude:  Optional[List[str]] = []
    detail:   bool = False

class RouteResponse(BaseModel):
    nodes: List[str]
    cost:  float
    detail: Optional[List[NodeAccumulated]] = None
    edges:  Optional[List[Tuple[str, str, float]]] = None
