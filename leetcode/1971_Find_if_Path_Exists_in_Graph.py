from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        stack = [source]
        visited = set()
        while stack:
            u = stack.pop()
            if u == destination:
                return True
            if u in visited:
                continue
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)
        return False
