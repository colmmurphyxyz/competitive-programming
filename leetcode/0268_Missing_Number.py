class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sorted = [ None for _ in range(len(nums)) ]
        for i in range(len(nums)):
            n = nums[i]
            if n < len(nums):
                sorted[n] = n
        print(sorted)
        for i in range(len(sorted)):
            if i != sorted[i]:
                return i
        return len(nums)
            
if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    print(s.missingNumber([0, 1]))
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
