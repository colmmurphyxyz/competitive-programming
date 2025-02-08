class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        r = [0] * (n + 1)
        r[0] = 0
        r[1] = 1
        r[2] = 1
        for i in range(3, n + 1):
            r[i] = r[i - 3] + r[i - 2] + r[i - 1]
        return r[-1]
    
if __name__ == "__main__":
    s = Solution()
    print("start")
    print(s.tribonacci(4))
    print(s.tribonacci(25))