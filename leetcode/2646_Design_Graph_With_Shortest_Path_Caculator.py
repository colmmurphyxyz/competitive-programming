from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self._adj = defaultdict(set)
        self._distances: dict[(int, int), int] = {}
        self._vertices = set()
        for src, dest, cost in edges:
            self._vertices.add(src)
            self._vertices.add(dest)
            self._adj[src].add(dest)
            if curr_dist := self._distances.get((src, dest)):
                self._distances[(src, dest)] = min(curr_dist, cost)
            else:
                self._distances[(src, dest)] = cost

    def addEdge(self, edge: list[int]) -> None:
        src, dest, cost = edge
        self._vertices.add(src)
        self._vertices.add(dest)
        self._adj[src].add(dest)
        if curr_dist := self._distances.get((src, dest)):
            self._distances[(src, dest)] = min(curr_dist, cost)
        else:
            self._distances[(src, dest)] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = { node: float("inf") for node in self._vertices }
        dist[node1] = 0
        pq = [(0, node1)]
        heapq.heapify(pq)
        visited = set()
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            for neighbor in self._adj[curr_node]:
                weight = self._distances[(curr_node, neighbor)]
                alt = curr_dist + weight
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    heapq.heappush(pq, (alt, neighbor))
        if (ret := dist[node2]) != float("inf"):
            return ret
        return -1
    
if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2)) # 6
    print(g.shortestPath(0, 3)) # -1
    g.addEdge([1, 3, 4])
    print(g.shortestPath(0, 3)) # 6



        