import heapq
import structlog

logger = structlog.get_logger(__name__)

def dijkstra(G, start, end, detail: bool = False):
    logger.info(
        "Iniciando algoritmo Dijkstra",
        nodo_inicio=start,
        nodo_fin=end,
        detalle=detail
    )

    dist = {node: float('inf') for node in G}
    prev = {node: None for node in G}
    dist[start] = 0.0

    heap = [(0.0, start)]
    visited = set()

    logger.debug("Estructuras inicializadas", distancias=dist, predecesores=prev)

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            logger.debug("Nodo ya visitado, se omite", nodo=u)
            continue
        visited.add(u)

        logger.debug("Nodo visitado", nodo=u, distancia_actual=d)

        if u == end:
            logger.info("Nodo destino alcanzado", nodo=u)
            break

        for v in sorted(G[u].keys()):
            if v in visited:
                continue
            w = G[u][v].get('weight', 1)
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
                logger.debug(
                    "Distancia actualizada",
                    nodo_vecino=v,
                    peso_arista=w,
                    nueva_distancia=nd,
                    predecesor=u
                )

    if dist[end] == float('inf'):
        logger.error("No se encontró camino", inicio=start, destino=end)
        raise ValueError(f"No se encontró camino de {start} a {end}")

    path = []
    u = end
    while u is not None:
        path.append(u)
        u = prev[u]
    path.reverse()

    logger.info("Camino óptimo encontrado", camino=path, costo_total=dist[end])

    if not detail:
        return path, dist[end]
    else:
        accumulated_list = [
            {"node": node, "accumulated": round(dist[node], 2)}
            for node in path
        ]
        edges_list = []
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            w = G[u][v].get('weight', 1)
            edges_list.append((u, v, w))

        logger.info(
            "Detalle de pesos acumulados y aristas generado",
            detalle=accumulated_list,
            aristas=edges_list
        )
        return path, dist[end], accumulated_list, edges_list
