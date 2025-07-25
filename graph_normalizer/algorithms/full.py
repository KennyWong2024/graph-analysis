import networkx as nx
from collections import deque

def bfs_full_traversal(G, start):
    visited = {start}
    queue = deque([start])
    order = []
    edges = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(G.neighbors(u)):
            if v not in visited:
                visited.add(v)
                queue.append(v)
                edges.append((u, v))

    T = nx.DiGraph()
    T.add_nodes_from(order)
    T.add_edges_from(edges)

    total = sum(G[u][v]['weight'] for u, v in T.edges())
    return list(T.nodes()), total

def dfs_full_traversal(G, start):
    visited = set()
    order = []
    edges = []

    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in sorted(G.neighbors(u)):
            if v not in visited:
                edges.append((u, v))
                dfs(v)

    dfs(start)

    T = nx.DiGraph()
    T.add_nodes_from(order)
    T.add_edges_from(edges)

    total = sum(G[u][v]['weight'] for u, v in T.edges())
    return list(T.nodes()), total
