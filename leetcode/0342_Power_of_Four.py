class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & (n - 1) or n == 0:
            return False
        even = True
        i = 1
        while True:
            if n & i:
                return even
            even = not even
            i <<= 1

    
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour(5))
    print(s.isPowerOfFour(1))
    print(s.isPowerOfFour(2))
    print(s.isPowerOfFour(6))
    print(s.isPowerOfFour(17))
    print(s.isPowerOfFour(0))