class Solution:
    def majorityElement(sel, nums: list[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))


            