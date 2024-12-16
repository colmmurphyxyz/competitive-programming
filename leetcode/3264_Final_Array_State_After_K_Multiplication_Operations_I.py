class Solution:
    
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            smallest_num: int = nums[0]
            smallest_idx: int = 0
            for i in range(len(nums)):
                if nums[i] < smallest_num:
                    smallest_num = nums[i]
                    smallest_idx = i
            nums[smallest_idx] = smallest_num * multiplier
        return nums
    
if __name__ == "__main__":
    s = Solution()
    print(s.getFinalState([2, 1, 3, 5, 6], 5, 2))
    print(s.getFinalState([1, 2], 3, 4))
    print(s.getFinalState([1], 4, 5))
