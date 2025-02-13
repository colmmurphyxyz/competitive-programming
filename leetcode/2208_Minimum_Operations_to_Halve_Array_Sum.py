import heapq

class Solution:
    def halveArray(self, nums: list[int]) -> int:
        array_sum = sum(nums)
        threshold = array_sum / 2
        nums = [ -num for num in nums ]
        heapq.heapify(nums)
        operations = 0
        while array_sum > threshold:
            a = heapq.heappop(nums)
            updated = a / 2
            array_sum += updated
            heapq.heappush(nums, updated)
            operations += 1
        return operations
    
if __name__ == "__main__":
    s = Solution()
    print(s.halveArray([5, 19, 8, 1]))
    print(s.halveArray([3, 8, 20]))

        