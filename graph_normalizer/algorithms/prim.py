import networkx as nx
import heapq
from typing import List, Tuple, Union
from networkx import Graph, DiGraph

def prim_tree_cost(
    G: Union[Graph, DiGraph],
    start: Union[str, None] = None
) -> Tuple[List[str], float, List[Tuple[str, str, float]]]:
    if start is None or start not in G.nodes():
        start_node = sorted(G.nodes())[0]
    else:
        start_node = start

    visited = {start_node}
    pq: List[Tuple[float, str, str]] = []
    for _, nbr, data in G.edges(start_node, data=True):
        heapq.heappush(pq, (data['weight'], start_node, nbr))

    total_cost = 0.0
    edges_added: List[Tuple[str, str, float]] = []
    nodes_order: List[str] = [start_node]

    while pq and len(visited) < G.number_of_nodes():
        weight, u, v = heapq.heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        total_cost += weight
        edges_added.append((u, v, weight))
        nodes_order.append(v)

        for _, nbr, data in G.edges(v, data=True):
            if nbr not in visited:
                heapq.heappush(pq, (data['weight'], v, nbr))

    return nodes_order, total_cost, edges_added
