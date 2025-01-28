class Solution:
    def connected_squares(self, grid: list[list[int]], source: tuple[int, int]) -> set[int]:
        visited = set()
        stack = [source]
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            adj = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for a in adj:
                if self.is_valid(grid, a) and a not in visited:
                    stack.append(a)
        return visited

    def is_valid(self, grid: list[list[int]], coord: tuple[int, int]) -> bool:
        i, j = coord
        if i < 0 or j < 0:
            return False
        m = len(grid)
        n = len(grid[0])
        if i >= m or j >= n:
            return False
        if grid[i][j] == 0:
            return False
        return True

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        largest: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if (i, j) in seen:
                    continue
                connected = self.connected_squares(grid, (i, j))
                seen |= connected
                largest = max(largest, len(connected))
        return largest

    
if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))