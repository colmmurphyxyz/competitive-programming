class Solution:
    def calculate(self, s: str) -> int:
        tokens = self._tokenize(s)
        _, res = self._evaluate(tokens, i=-1)
        return res
    
    def _evaluate(self, tokens: list[int], i: int = 0) -> tuple[int, int]:
        operand = result = 0
        next_sign = 1 # 1 for positive, -1 for negative
        while i < len(tokens) - 1:
            i += 1
            token = tokens[i]
            if token.isdigit():
                operand = int(token)
            elif token == "(":
                end, operand = self._evaluate(tokens, i)
                i = end
            elif token == ")":
                break
            else:
                result += next_sign * operand
                next_sign = 1 if token == "+" else -1
                operand = 0
        return i, result + (next_sign * operand)
    
    def _tokenize(self, s: str) -> list[str]:
        tokens = []
        i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            elif s[i].isdigit():
                subtotal = s[i]
                i += 1
                while i < len(s) and s[i].isdigit():
                    subtotal += s[i]
                    i += 1
                tokens.append(subtotal)
            else:
                tokens.append(s[i])
                i += 1
        return tokens
        
if __name__ == "__main__":
    s = Solution()
    # print(s.calculate("1 + 1 + - 4")) # -2
    print(s.calculate("8 - 6 - 3"))
    print(s.calculate("2 - 1 + 2")) # 3
    print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 22
    print(s.calculate("1 + (2 + 3) + (4 + 5)")) # 15
        