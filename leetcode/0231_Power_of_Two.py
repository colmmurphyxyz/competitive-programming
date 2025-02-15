class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        def aux(k: int) -> bool:
            if k & 1:
                return k == 1
            return aux(k // 2)
        return aux(n)
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(1))
    print(s.isPowerOfTwo(16))
    print(s.isPowerOfTwo(3))
    print(s.isPowerOfTwo(2))
    print(s.isPowerOfTwo(1 << 63))
    print(s.isPowerOfTwo((1 << 63) - 1))