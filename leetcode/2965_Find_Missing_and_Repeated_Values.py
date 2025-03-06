class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid) ** 2
        missing = (n * (n + 1)) // 2
        seen = set()
        repeated = -1
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                    continue
                seen.add(num)
                missing -= num
        return [repeated, missing]
    
if __name__ == "__main__":
    s = Solution()
    print(s.findMissingAndRepeatedValues([[1,3],[2,2]]))
    print(s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))
