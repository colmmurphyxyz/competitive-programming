class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        delta = 0
        i: int = 0
        while i < len(nums):
            if nums[i] == 0:
                delta += 1
            else:
                nums[i], nums[i - delta] = nums[i - delta], nums[i]
            i += 1

if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)

