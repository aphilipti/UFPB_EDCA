def dijkstra(graph):

    n = len(graph)

    dist = [float('inf')] * n
    visited = [False] * n

    dist[0] = 0

    for _ in range(n):

        u = -1

        for v in range(n):

            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v

        visited[u] = True

        for v in range(n):

            weight = graph[u][v]

            if weight > 0 and not visited[v]:

                new_dist = dist[u] + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist

    return dist[n - 1]