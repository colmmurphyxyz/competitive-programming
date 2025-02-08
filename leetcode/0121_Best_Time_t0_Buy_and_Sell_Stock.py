class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_after = prices.copy()
        for i in range(len(prices) - 2, -1, -1):
            max_after[i] = max(max_after[i], max_after[i + 1])
        best = 0
        for i in range(len(prices) - 1):
            buy_price = prices[i]
            profit = max_after[i + 1] - buy_price
            best = max(best, profit)
        return best

    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
        