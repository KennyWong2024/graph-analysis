from pydantic import BaseModel
from typing import List, Optional

class RouteRequest(BaseModel):
    start: str
    end:   Optional[str] = None
    algo:  str
    directed: bool = False 
          
class RouteResponse(BaseModel):
    nodes: List[str]      
    cost:  float
