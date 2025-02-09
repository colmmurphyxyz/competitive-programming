class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = [None] * (n + 1)
        memo[0] = 0
        memo[1] = 0
        for i in range(2, n + 1):
            memo[i] = min(
                memo[i - 1] + cost[i - 1],
                memo[i - 2] + cost[i - 2]
            )
        return memo[-1]

    
if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))