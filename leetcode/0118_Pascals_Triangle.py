class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        if numRows == 2:
            return triangle
        def dp(prev: list[int]) -> list[int]:
            row = [0] * (len(prev) + 1)
            row[0] = 1
            row[-1] = 1
            for i in range(1, len(prev)):
                row[i] = prev[i - 1] + prev[i]
            return row
        for j in range(2, numRows):
            triangle.append(dp(triangle[j - 1]))
        return triangle
    
if __name__ == "__main__":
    s = Solution()
    print(s.generate(1))
    print(s.generate(5))