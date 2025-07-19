import networkx as nx

def build_graph(edges):
    G = nx.Graph()
    for edge in edges:
        src = edge['source']
        tgt = edge['target']
        w = edge['weight']
        G.add_edge(src, tgt, weight=w)
    return G
