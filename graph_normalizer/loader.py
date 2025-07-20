import logging
import networkx as nx
from typing import List, Dict, Union
from networkx import Graph, DiGraph

logger = logging.getLogger(__name__)

Edge = Dict[str, Union[str, float]]

def build_graph(edges: List[Edge], directed: bool = False) -> Union[Graph, DiGraph]:
    graph_type = 'DiGraph' if directed else 'Graph'
    logger.debug(f"Starting build_graph: constructing {graph_type} with {len(edges)} edges")

    G = nx.DiGraph() if directed else nx.Graph()

    for edge in edges:
        try:
            src = edge['source']
            tgt = edge['target']
            w = edge['weight']
        except KeyError as e:
            logger.warning(f"Skipping malformed edge {edge}: missing {e}")
            continue

        G.add_edge(src, tgt, weight=w)

    logger.debug(
        f"Finished build_graph: resulting {graph_type} has "
        f"{G.number_of_nodes()} nodes and {G.number_of_edges()} edges"
    )
    return G