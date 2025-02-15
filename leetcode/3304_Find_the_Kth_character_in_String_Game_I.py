class Solution:
    def _get_next_char(self, s: str) -> str:
        return chr(97 + ((ord(s) -96) % 26))
    def kthCharacter(self, k: int) -> str:
        word = ["a"]
        while len(word) < k:
            tail = list(map(self._get_next_char, word))
            word = word + tail
            print(f"{word=}")
        return word[k - 1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.kthCharacter(5))