from pydantic import BaseModel
from typing import List

class RouteRequest(BaseModel):
    start: str
    end: str
    algo: str  # Algoritmos

class RouteResponse(BaseModel):
    path: List[str]
    cost: float
