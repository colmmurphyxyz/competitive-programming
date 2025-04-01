class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        def bulid_permutations(xs: set[int], curr: list[int]):
            if len(xs) == 0:
                permutations.append(curr)
                return
            for x in xs:
                bulid_permutations(xs.difference({x}), curr + [x])
        bulid_permutations(set(nums), [])
        return permutations
    
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.permute([0, 1]))
    print(s.permute([1]))