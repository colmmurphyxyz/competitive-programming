class Solution:
    def dfs(self, grid: list[list[int]], source: tuple[int, int]) -> set[int]:
        stack = [source]
        visited = set()
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            adj = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for a in adj:
                if self.is_valid(grid, a) and a not in visited:
                    stack.append(a)
        return visited
    
    def is_valid(self, grid: list[list[int]], coord: tuple[int, int]) -> bool:
        x, y = coord
        m = len(grid)
        n = len(grid[0])
        if x < 0 or y < 0:
            return False
        if x >= m or y >= n:
            return False
        if grid[x][y] == 0:
            return False
        return True
        

    def findMaxFish(self, grid: list[list[int]]) -> int:
        max_fish = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if (i, j) in seen:
                    continue
                squares = self.dfs(grid, (i, j))
                seen |= squares
                fish = sum(list(map(lambda c: grid[c[0]][c[1]], squares)))
                max_fish = max(max_fish, fish)
        return max_fish
    
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
    print(s.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))