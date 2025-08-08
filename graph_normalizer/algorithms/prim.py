import networkx as nx
import heapq
from typing import List, Tuple, Union, Optional, Dict
from networkx import Graph, DiGraph
import structlog

logger = structlog.get_logger(__name__)

def prim_tree_cost(
    G: Union[Graph, DiGraph],
    start: Optional[str] = None,
    detail: bool = False
):
    if G.number_of_nodes() == 0:
        logger.error("El grafo no tiene nodos")
        raise ValueError("El grafo está vacío")

    if start is None or start not in G.nodes():
        start_node = sorted(G.nodes())[0]
        motivo = "no_proporcionado_o_inválido"
    else:
        start_node = start
        motivo = "proporcionado"

    logger.info(
        "Iniciando algoritmo Prim",
        nodo_inicio=start_node,
        motivo_seleccion_inicio=motivo,
        dirigido=isinstance(G, nx.DiGraph),
        nodos=G.number_of_nodes(),
        aristas=G.number_of_edges(),
        detalle=detail
    )

    visited = {start_node}
    pq: List[Tuple[float, str, str]] = []

    for _, nbr, data in G.edges(start_node, data=True):
        w = data.get('weight', 1)
        heapq.heappush(pq, (w, start_node, nbr))
    logger.debug("Aristas iniciales en la cola", cantidad=len(pq), nodo=start_node)

    total_cost = 0.0
    edges_added: List[Tuple[str, str, float]] = []
    nodes_order: List[str] = [start_node]

    while pq and len(visited) < G.number_of_nodes():
        weight, u, v = heapq.heappop(pq)

        if v in visited:
            logger.debug("Arista descartada (destino ya visitado)", origen=u, destino=v, peso=weight)
            continue

        visited.add(v)
        total_cost += weight
        edges_added.append((u, v, weight))
        nodes_order.append(v)

        logger.info(
            "Arista seleccionada para el MST",
            origen=u,
            destino=v,
            peso=weight,
            costo_total_parcial=total_cost,
            nodos_en_mst=len(visited)
        )

        for _, nbr, data in G.edges(v, data=True):
            if nbr not in visited:
                w = data.get('weight', 1)
                heapq.heappush(pq, (w, v, nbr))
        logger.debug(
            "Aristas añadidas desde el nuevo nodo",
            nodo=v,
            nuevas_aristas=sum(1 for _ in G.edges(v)) 
        )

    if len(visited) < G.number_of_nodes():
        logger.warning(
            "Grafo no conexo: el MST cubre solo la componente del nodo inicial",
            nodos_en_mst=len(visited),
            nodos_totales=G.number_of_nodes()
        )

    logger.info(
        "MST construido con Prim",
        costo_total=total_cost,
        nodos_en_mst=len(nodes_order),
        aristas_en_mst=len(edges_added)
    )

    if not detail:
        return nodes_order, total_cost, edges_added
    else:
        accumulated_list: List[Dict[str, float]] = [{"node": nodes_order[0], "accumulated": 0.0}]
        accumulated_value = 0.0
        for (_, v, w) in edges_added:
            accumulated_value += w
            accumulated_list.append({"node": v, "accumulated": round(accumulated_value, 2)})

        logger.info("Detalle de pesos acumulados generado", detalle=accumulated_list)
        return nodes_order, total_cost, edges_added, accumulated_list
