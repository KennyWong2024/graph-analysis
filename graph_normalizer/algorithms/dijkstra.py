import heapq

def dijkstra(G, start, end):
    dist = {node: float('inf') for node in G}
    prev = {node: None for node in G}
    dist[start] = 0.0

    heap = [(0.0, start)]

    visited = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        if u == end:
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

    if dist[end] == float('inf'):
        raise ValueError(f"No se encontró camino de {start} a {end}")

    path = []
    u = end
    while u is not None:
        path.append(u)
        u = prev[u]
    path.reverse()

    return path, dist[end]
