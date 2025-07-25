import os
import httpx
from graph_normalizer.loader import build_graph
from graph_normalizer.algorithms.bfs import bfs_path_cost
from graph_normalizer.algorithms.dfs import dfs_path_cost
from graph_normalizer.algorithms.full import bfs_full_traversal, dfs_full_traversal
from graph_normalizer.algorithms.prim import prim_tree_cost
from graph_normalizer.algorithms.dijkstra import dijkstra
from .schemas import RouteRequest, RouteResponse

INGEST_URL = os.getenv("INGEST_SERVICE_URL")

async def compute_route(req: RouteRequest) -> RouteResponse:
    r = httpx.get(INGEST_URL)
    r.raise_for_status()
    edges = r.json()

    G = build_graph(edges, directed=req.directed)

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
        nodes, cost, _ = prim_tree_cost(G, start=req.start)

    elif req.algo == "dijkstra":
        if not req.end:
            raise ValueError("Dijkstra requires a destination node (`end`).")
        nodes, cost = dijkstra(G, req.start, req.end)

    else:
        raise ValueError(f"Unsupported algorithm: {req.algo}")

    return RouteResponse(nodes=nodes, cost=cost)
