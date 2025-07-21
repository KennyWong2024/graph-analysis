import logging
import networkx as nx
from typing import List, Dict, Union
from networkx import Graph, DiGraph

logger = logging.getLogger(__name__)

Edge = Dict[str, Union[str, float]]

def build_graph(edges: List[Edge], directed: bool = False) -> Union[Graph, DiGraph]:
    tipo_grafo = 'dirigido' if directed else 'no dirigido'
    logger.debug(f"Iniciando construcción de grafo {tipo_grafo} con {len(edges)} aristas")

    G = nx.DiGraph() if directed else nx.Graph()

    for edge in edges:
        try:
            src = edge['source']
            tgt = edge['target']
            w = edge['weight']
        except KeyError as e:
            logger.warning(f"Omitiendo arista mal formateada {edge}: falta la clave {e}")
            continue

        G.add_edge(src, tgt, weight=w)

    logger.debug(
        f"Finalizada construcción de grafo {tipo_grafo}: "
        f"{G.number_of_nodes()} nodos, {G.number_of_edges()} aristas"
    )
    return G
