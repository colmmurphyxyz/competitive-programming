class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        candidate = word
        while candidate in sequence:
            k += 1
            candidate += word
        return k - 1
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxRepeating("ababc", "ab"))
    print(s.maxRepeating("ababc", "ba"))
    print(s.maxRepeating("ababc", "ac"))
