class Solution:
    def decodeString(self, s: str) -> str:
        ret, _ = self.decode(s, 0)
        return ret

    def decode(self, s: str, i: int) -> tuple[str, int]:
        quantifier = 0
        pattern = ""
        while i < len(s):
            curr = s[i]
            if curr.isdigit():
                quantifier *= 10
                quantifier += int(curr)
            elif curr == "[":
                val, k = self.decode(s, i + 1)
                pattern += quantifier * val
                quantifier = 0
                i = k
            elif curr == "]":
                if quantifier == 0:
                    return (pattern, i)
                return (quantifier * pattern, i)
            else:
                pattern += curr
            i += 1
        return pattern, i
    
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))
                 
        
