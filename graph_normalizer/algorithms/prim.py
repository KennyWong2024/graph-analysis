import networkx as nx

def prim_tree_cost(G):
    T = nx.minimum_spanning_tree(G, weight='weight')
    total = sum(data['weight'] for _, _, data in T.edges(data=True))
    nodes = list(T.nodes())
    return nodes, total
