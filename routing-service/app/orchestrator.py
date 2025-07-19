import httpx
from graph_normalizer.loader import build_graph
from graph_normalizer.algorithms.bfs import bfs_path_cost
from graph_normalizer.algorithms.dfs import dfs_path_cost
from graph_normalizer.algorithms.prim import prim_tree_cost
from .schemas import RouteRequest, RouteResponse

INGEST_URL = "http://localhost:8000/export-graph"

async def compute_route(req: RouteRequest) -> RouteResponse:
    # 1) Obtener aristas
    r = httpx.get(INGEST_URL)
    r.raise_for_status()
    edges = r.json()

    # 2) Construir grafo
    G = build_graph(edges)

    # 3) Ejecutar algoritmo
    if req.algo == "bfs":
        path, cost = bfs_path_cost(G, req.start, req.end)
    elif req.algo == "dfs":
        path, cost = dfs_path_cost(G, req.start, req.end)
    elif req.algo == "prim":
        path, cost = prim_tree_cost(G)
    else:
        raise ValueError("Algoritmo no soportado")

    # 4) Devolver
    return RouteResponse(path=path, cost=cost)
