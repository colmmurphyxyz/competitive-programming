class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        search_target: int = 0
        for i in range(len(t)):
            if t[i] == s[search_target]:
                search_target += 1
                if search_target >= len(s):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))