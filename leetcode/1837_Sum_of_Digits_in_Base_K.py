from functools import reduce

class Solution:
    def sumDigits(self, s: str) -> int:
        return reduce(lambda acc, digit: acc + int(digit), s, 0)
    
    def sumDigitsBase10(self, n: int) -> int:
        total = 0
        while n:
            total += n % 10
            n = n // 10
        return total

    def sumBase(self, n: int, k: int) -> int:
        if k == 10:
            return self.sumDigitsBase10(n)
        # base K string will be backwards, but that's not relevant here
        baseK = ""
        while n:
            baseK += str(n % k)
            n = n // k
        print("baseK", baseK)
        return self.sumDigits(baseK)

if __name__ == "__main__":
    s = Solution()
    print(s.sumBase(34, 6))
    print(s.sumBase(10, 10))