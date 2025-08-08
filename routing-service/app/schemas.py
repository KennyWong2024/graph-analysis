from pydantic import BaseModel
from typing import List, Optional

class RouteRequest(BaseModel):
    start:    str
    end:      Optional[str] = None
    algo:     str
    directed: bool = False
    exclude:  Optional[List[str]] = [] 

class RouteResponse(BaseModel):
    nodes: List[str]
    cost:  float
