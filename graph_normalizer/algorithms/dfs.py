def dfs_path_cost(G, start, end):
    visited = set()

    def dfs(node, path, cost):
        if node == end:
            return path, cost
        visited.add(node)
        for neighbor, data in G[node].items():
            if neighbor not in visited:
                w = data.get('weight', 1)
                result = dfs(neighbor, path + [neighbor], cost + w)
                if result:
                    return result
        return None

    result = dfs(start, [start], 0.0)
    if result:
        return result
    raise ValueError(f"No se encontró camino DFS de {start} a {end}")