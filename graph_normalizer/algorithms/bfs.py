from collections import deque

def bfs_path_cost(G, start, end):
    visited = {start}
    queue = deque([(start, [start], 0.0)])

    while queue:
        node, path, cost = queue.popleft()
        if node == end:
            return path, cost
        for neighbor, data in G[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                w = data.get('weight', 1)
                queue.append((neighbor, path + [neighbor], cost + w))
    raise ValueError(f"No se encontró camino BFS de {start} a {end}")
