import httpx
from graph_normalizer.loader import build_graph
from graph_normalizer.algorithms.bfs import bfs_path_cost
from graph_normalizer.algorithms.dfs import dfs_path_cost
from graph_normalizer.algorithms.prim import prim_tree_cost
from graph_normalizer.algorithms.full import bfs_full_traversal, dfs_full_traversal
from .schemas import RouteRequest, RouteResponse

INGEST_URL = "http://localhost:8000/export-graph"

async def compute_route(req: RouteRequest) -> RouteResponse:
    # Obtener aristas
    r = httpx.get(INGEST_URL)
    r.raise_for_status()
    edges = r.json()

    # Construir grafo
    G = build_graph(edges, directed=req.directed)

    # Ejecutar algoritmo
    if req.algo == "bfs":
        if req.end:
            nodes, cost = bfs_path_cost(G, req.start, req.end)
        else:
            nodes, cost = bfs_full_traversal(G, req.start)

    elif req.algo == "dfs":
        if req.end:
            nodes, cost = dfs_path_cost(G, req.start, req.end)
        else:
            nodes, cost = dfs_full_traversal(G, req.start)

    elif req.algo == "prim":
        nodes, cost = prim_tree_cost(G)

    else:
        raise ValueError("Algoritmo no soportado")

    # Devolver
    return RouteResponse(nodes=nodes, cost=cost)
