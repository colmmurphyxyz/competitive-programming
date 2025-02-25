class Solution:
    def invert(self, s: str) -> str:
        inverted: str = ""
        for c in s:
            inverted += "0" if c == "1" else "1"
        return inverted
    
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while len(s) < k:
            s = s + "1" + self.invert(s)[::-1]
        return s[k - 1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.findKthBit(3, 1))
    print(s.findKthBit(4, 11))