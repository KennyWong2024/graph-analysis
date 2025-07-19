from pydantic import BaseModel

class GraphEdge(BaseModel):
    source: str
    target: str
    weight: float
