class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        counts = {}
        lonely = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num in nums:
            if counts[num] == 1 and counts.get(num - 1) is None and counts.get(num + 1) is None:
                lonely.append(num)
        return lonely
    
if __name__ == "__main__":
    s = Solution()
    print(s.findLonely([10, 6, 5, 8]))
    print(s.findLonely([1, 3, 5, 3]))