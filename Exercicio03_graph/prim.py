def prim(graph):

    n = len(graph)

    selected = [False] * n
    min_edge = [float('inf')] * n

    min_edge[0] = 0

    total = 0

    for _ in range(n):

        u = -1

        for v in range(n):

            if not selected[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v

        selected[u] = True
        total += min_edge[u]

        for v in range(n):

            weight = graph[u][v]

            if weight > 0 and not selected[v] and weight < min_edge[v]:
                min_edge[v] = weight

    return total