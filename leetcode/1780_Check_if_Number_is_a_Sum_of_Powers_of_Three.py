class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            n, remainder = divmod(n, 3)
            if remainder == 2:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.checkPowersOfThree(12))
    print(s.checkPowersOfThree(91))
    print(s.checkPowersOfThree(21))
        