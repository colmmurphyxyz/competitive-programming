from math import floor, ceil

class Solution:
    # def countGoodNumbers(self, n: int) -> int:
    #     MOD = (10 ** 9) + 7 
    #     i = 0
    #     total = 1
    #     even = True
    #     while i < n:
    #         if even:
    #             total = (total * 5) % MOD
    #             even = False
    #         else:
    #             total = (total * 4) % MOD
    #             even = True
    #         i += 1
    #     return total

    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        if n == 1:
            return 5
        if n % 2 == 0:
            return (pow(5, n // 2, MOD) * pow(4, n // 2, MOD)) % MOD
        return (pow(5, ceil(n / 2), MOD) * pow(4, floor(n / 2), MOD)) % MOD
    
if __name__ == "__main__":
    s = Solution()
    print(s.countGoodNumbers(1))
    print(s.countGoodNumbers(2))
    print(s.countGoodNumbers(3))
    print(s.countGoodNumbers(4))
    print(s.countGoodNumbers(50))
    print(s.countGoodNumbers(10 ** 15))
