class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n / 3)
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(3))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(1))
    print(s.isPowerOfThree(-1))