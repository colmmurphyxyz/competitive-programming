import heapq

class Solution:

    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = list(zip(nums, range(len(nums))))
        heapq.heapify(heap)
        for _ in range(k):
            _, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))
        return nums
    
if __name__ == "__main__":
    s = Solution()
    print(s.getFinalState([2, 1, 3, 5, 6], 5, 2))
    print(s.getFinalState([1, 2], 3, 4))
    print(s.getFinalState([1], 4, 5))
