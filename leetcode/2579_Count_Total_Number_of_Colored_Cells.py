class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        k = (2 * n) - 1
        ans = k
        k -= 2
        while k > 0:
            ans += 2 * k
            k -= 2
        return ans
    
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        print(i, s.coloredCells(i))