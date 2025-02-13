import heapq

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        total_stones = sum(piles)
        removed_stones = 0
        piles = [ -pile for pile in piles ]
        heapq.heapify(piles)
        for _ in range(k):
            p = heapq.heappop(piles)
            removed = -p // 2
            updated = p + removed
            removed_stones += removed
            heapq.heappush(piles, updated)
        return total_stones - removed_stones
    
if __name__ == "__main__":
    s = Solution()
    # print(s.minStoneSum([5, 4, 9], 2))
    # print(s.minStoneSum([4, 3, 6, 7], 3))
    print(s.minStoneSum([1], 100))
        