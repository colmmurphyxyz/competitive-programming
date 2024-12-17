class Solution:
    
    def compress(self, chars: list[str]) -> int:
        i: int = 0
        compressed_len: int = 0
        while i < len(chars):
            group_len: int = 1
            while (i + group_len < len(chars) and chars[i + group_len] == chars[i]):
                group_len += 1
            chars[compressed_len] = chars[i]
            compressed_len += 1
            if group_len > 1:
                n = str(group_len)
                chars[compressed_len:compressed_len + len(n)] = list(n)
                compressed_len += len(n)
            i += group_len
        return compressed_len

    
if __name__ == "__main__":
    s = Solution()
    chars = list("aabbccc")
    print(s.compress(chars))
    print(chars)
    chars = list("a")
    print(s.compress(chars))
    print(chars)
    chars = list("abbbbbbbbbbbb")
    print(s.compress(chars))
    print(chars)
