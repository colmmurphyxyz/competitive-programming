class Solution:
    def climbStairs(self, n: int) -> int:
        r = [0] * n
        r[0] = 1
        r[1] = 2
        for i in range(2, n):
            r[i] = r[i - 1] + r[i - 2]
        return r[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(6))

