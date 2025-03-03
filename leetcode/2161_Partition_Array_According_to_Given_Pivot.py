class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        partitioned = [ None for _ in range(len(nums)) ]
        left = 0
        right = len(nums) - 1
        pivot_count = 0
        for x in nums:
            if x < pivot:
                partitioned[left] = x
                left += 1
            elif x > pivot:
                partitioned[right] = x
                right -= 1
            else:
                pivot_count += 1
        for _ in range(pivot_count):
            partitioned[left] = pivot
            left += 1
        right = len(partitioned) - 1
        while right > left:
            partitioned[left], partitioned[right] = partitioned[right], partitioned[left]
            left += 1
            right -= 1
        return partitioned
    
if __name__ == "__main__":
    s = Solution()
    print(s.pivotArray([9,12,5,10,14,3,10], 10))
    print(s.pivotArray([-3,4,3,2], 2))
    

