class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                y = nums[j]
                if x != y:
                    continue
                if (i * j) % k == 0:
                    # print(f"{i=} {j=} {nums[i]=} {nums[j]=}")
                    count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countPairs([3, 1, 2, 2, 2, 1, 3], 2))
    print(s.countPairs([1, 2, 3, 4], 1))