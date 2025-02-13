import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while True:
            a = heapq.heappop(nums)
            if a >= k:
                return operations
            b = heapq.heappop(nums)
            updated = min(a, b) * 2 + max(a, b)
            heapq.heappush(nums, updated)
            operations += 1
    
if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2, 11, 10, 1, 3], 10))
    print(s.minOperations([1, 1, 2, 4, 9], 20))
        