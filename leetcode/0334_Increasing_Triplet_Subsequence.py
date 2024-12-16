class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        m1 = float("inf")
        m2 = float("inf")
        for num in nums:
            if num <= m1:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1, 2, 3, 4, 5]))
    print(s.increasingTriplet([5, 4, 3, 2, 1]))
    print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))