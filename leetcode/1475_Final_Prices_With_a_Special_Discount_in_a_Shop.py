class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = prices.copy()
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] -= prices[i]
            stack.append(i)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.finalPrices([8, 4, 6, 2, 3]))
    print(s.finalPrices([1, 2, 3, 4, 5]))
    print(s.finalPrices([10, 1, 1, 6]))