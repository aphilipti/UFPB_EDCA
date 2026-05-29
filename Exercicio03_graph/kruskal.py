class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


def kruskal(graph):

    n = len(graph)

    edges = []

    for i in range(n):
        for j in range(i + 1, n):

            edges.append((graph[i][j], i, j))

    edges.sort()

    uf = UnionFind(n)

    total = 0
    count = 0

    for weight, u, v in edges:

        if uf.find(u) != uf.find(v):

            uf.union(u, v)

            total += weight
            count += 1

            if count == n - 1:
                break

    return total