class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        r = [0] * (n + 1)
        r[0] = 0
        r[1] = 1
        for i in range(2, n + 1):
            r[i] = r[i - 2] + r[i - 1]
        return r[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))