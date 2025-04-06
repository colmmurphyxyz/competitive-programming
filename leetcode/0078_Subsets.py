class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        self.dfs(nums, [], ans)
        return ans
    
    def dfs(self, nums: list[int], path: list[int], ans: list[list[int]]) -> None:
        if len(nums) == 0:
            ans.append(path)
            return
        self.dfs(nums[1:], path, ans)
        self.dfs(nums[1:], path + [nums[0]], ans)

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subsets([0]))
