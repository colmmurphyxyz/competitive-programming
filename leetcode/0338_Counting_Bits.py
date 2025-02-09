class Solution:

    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i // 2]
            if i & 1 > 0:
                dp[i] += 1
        return dp

if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
                
