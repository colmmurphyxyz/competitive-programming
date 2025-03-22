from heapq import heappush, heappop,  heapify

class Solution:
    def adj(self, i: int, j: int, m: int, n: int) -> list[tuple[int, int]]:
        adjacent = []
        if i > 0:
            adjacent.append((i - 1, j))
        if i < m - 1:
            adjacent.append((i + 1, j))
        if j > 0:
            adjacent.append((i, j - 1))
        if j < n - 1:
            adjacent.append((i, j + 1))
        return adjacent

    def minimumObstacles(self, grid: list[list[int]]) -> int:
        # run dijkstra's to find min cost
        # cost to move from U to V is the number of obstacles in the way
        # cost between two adjacent nodes is 1 if dest is an obstacle, 0 otherwise
        m = len(grid)
        n = len(grid[0])
        distances = self.dijkstra(grid, (0, 0))
        return distances[(m - 1, n - 1)]

    def dijkstra(self, grid: list[list[int]], source: tuple[int, int]) -> dict[tuple[int, int], int]:
        m = len(grid)
        n = len(grid[0])
        distances = {}
        for i in range(m):
            for j in range(n):
                distances[(i, j)] = float("inf")
        distances[source] = 0
        pq = [(0, source)]
        heapify(pq)
        visited = set()
        while pq:
            curr_dist, (i, j) = heappop(pq)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for x, y in self.adj(i, j, m, n):
                cost = grid[x][y]
                alt = curr_dist + cost
                if alt < distances[(x, y)]:
                    distances[(x, y)] = alt
                    heappush(pq, (alt, (x, y)))
        return distances
        
if __name__ == "__main__":
    s = Solution()
    print(s.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
    print(s.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))