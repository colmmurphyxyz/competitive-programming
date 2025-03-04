class Solution:
    # 1 <= nums.length <= 10^5
    def firstMissingPositive(self, nums: list[int]) -> int:
        first = 1
        # seen will hold at most 10^5 elems due to input constraints.
        # Technically constant space
        seen = set()
        for num in nums:
            if num <= 0 or num > (10 ** 5) + 1:
                continue
            seen.add(num)
            if num == first:
                first += 1
                while first in seen:
                    first += 1
        return first
    
if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    arr = [ i for i in range(1, 10 ** 5 + 1) ]
    print(s.firstMissingPositive(arr))
        