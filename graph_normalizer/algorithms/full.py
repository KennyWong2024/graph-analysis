import networkx as nx

def bfs_full_traversal(G, start):
    T = nx.bfs_tree(G, start)
    total = sum(G[u][v]['weight'] for u, v in T.edges())
    return list(T.nodes()), total

def dfs_full_traversal(G, start):
    T = nx.dfs_tree(G, start)
    total = sum(G[u][v]['weight'] for u, v in T.edges())
    return list(T.nodes()), total
