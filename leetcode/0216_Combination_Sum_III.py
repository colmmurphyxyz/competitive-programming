class Solution:
    # def combinationSum3(self, k: int, n: int) -> list[list[int]]:
    #     valid_combinations: set[set[int]] = set()
    #     def build(nums: set[int], curr: set[int], curr_sum: int, curr_len: int):
    #         if curr_len == k:
    #             if curr_sum == n:
    #                 valid_combinations.add(curr)
    #             return
    #         if curr_sum > n:
    #             return
    #         for num in nums:
    #             build(nums.difference({num}), curr | {num}, curr_sum + num, curr_len + 1)
    #     build({1, 2, 3, 4, 5, 6, 7, 8, 9}, frozenset(), 0, 0)
    #     return list(map(list, valid_combinations))

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ret = []
        self.dfs([1, 2, 3, 4, 5, 6, 7, 8, 9], k, n, [], ret)
        return ret

    def dfs(self, nums: list[int], k: int, n: int, path: list, ret: list[list[int]]) -> None:
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k - 1, n - nums[i], path + [nums[i]], ret)
    
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))

