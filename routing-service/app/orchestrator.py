import os
import httpx
import structlog

from graph_normalizer.loader import build_graph
from graph_normalizer.algorithms.bfs import bfs_path_cost
from graph_normalizer.algorithms.dfs import dfs_path_cost
from graph_normalizer.algorithms.full import bfs_full_traversal, dfs_full_traversal
from graph_normalizer.algorithms.prim import prim_tree_cost
from graph_normalizer.algorithms.dijkstra import dijkstra
from .schemas import RouteRequest, RouteResponse

INGEST_URL = os.getenv("INGEST_SERVICE_URL")

logger = structlog.get_logger(__name__)

async def compute_route(req: RouteRequest) -> RouteResponse:
    inicio_original = req.start
    destino_original = req.end
    req.start = req.start.upper()
    req.end = req.end.upper() if req.end else None
    req.exclude = [e.upper() for e in req.exclude] if req.exclude else []

    logger.info(
        "Parámetros de ruta normalizados",
        inicio_original=inicio_original,
        inicio_normalizado=req.start,
        destino_original=destino_original,
        destino_normalizado=req.end,
        excluir=req.exclude,
        algoritmo=req.algo,
        dirigido=req.directed
    )

    logger.info("Solicitando grafo a ingest-service", url=INGEST_URL)
    response = httpx.get(INGEST_URL)
    response.raise_for_status()
    edges = response.json()
    logger.info("Grafo recibido", total_aristas=len(edges))

    if req.exclude:
        antes = len(edges)
        edges = [
            e for e in edges
            if e.get("source").upper() not in req.exclude
               and e.get("target").upper() not in req.exclude
        ]
        logger.info(
            "Aristas filtradas",
            cantidad_original=antes,
            cantidad_filtrada=len(edges),
            excluir=req.exclude
        )

    G = build_graph(edges, directed=req.directed)
    logger.info(
        "Grafo construido",
        nodos=G.number_of_nodes(),
        aristas=G.number_of_edges(),
        dirigido=req.directed
    )

    logger.info("Iniciando ejecución del algoritmo", algoritmo=req.algo)
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
            logger.error("Error: Dijkstra requiere un nodo destino (`end`)")
            raise ValueError("Dijkstra requires a destination node (`end`).")
        nodes, cost = dijkstra(G, req.start, req.end)

    else:
        logger.error("Algoritmo no soportado", algoritmo=req.algo)
        raise ValueError(f"Unsupported algorithm: {req.algo}")

    logger.info("Ruta calculada con éxito", nodos=nodes, costo=cost)
    return RouteResponse(nodes=nodes, cost=cost)
