import heapq
from math import sqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        total_gifts = 0
        for i, g in enumerate(gifts):
            total_gifts += g
            gifts[i] = -g
        heapq.heapify(gifts)
        for _ in range(k):
            top = -heapq.heappop(gifts)
            updated = int(sqrt(top))
            total_gifts -= (top - updated)
            heapq.heappush(gifts, -updated)
        return total_gifts
    
if __name__ == "__main__":
    s = Solution()
    print(s.pickGifts([25, 64, 9, 4, 100], 4))
    print(s.pickGifts([1, 1, 1, 1], 4))