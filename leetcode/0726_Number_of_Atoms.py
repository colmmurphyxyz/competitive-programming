import re
from copy import copy
from functools import reduce

ATOM_RE = r"[A-Z][a-z]*"

tokens_re = re.compile(
    r"[A-Z][a-z]*"
    r"|[1-9][0-9]*"
    r"|\(|\)"
)

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tokens = tokens_re.findall(formula)
        count, _ = self.get_counts(tokens, 0)
        atoms = list(count.items())
        atoms.sort(key=lambda x: x[0])
        ret = ""
        for a, c in atoms:
            ret += a
            if c > 1:
                ret += str(c)
        return ret
        

    def get_counts(self, tokens: list[str], i: int) -> tuple[dict[str, int], int]:
        count = {}
        while i < len(tokens):
            curr = tokens[i]
            if curr == "(":
                grouped, k = self.get_counts(tokens, i + 1)
                i = k
                if self.is_quantifier(tokens, i + 1):
                    q = int(tokens[i + 1])
                    i += 1
                    grouped = { key: value * q for (key, value) in grouped.items() }
                count = self.merge_dicts(count, grouped)
            elif curr == ")":
                return count, i
            elif self.is_atom(tokens, i):
                atom = tokens[i]
                q = 1
                if self.is_quantifier(tokens, i + 1):
                    q = int(tokens[i + 1])
                    i += 1
                if atom not in count.keys():
                    count[atom] = 0
                count[atom] += q
            i += 1
        return count, i

    def merge_dicts(self, lhs: dict[str: int], rhs: dict[str, int]) -> dict[str, int]:
        merged = copy(lhs)
        for key, value in rhs.items():
            if key in merged.keys():
                merged[key] += value
            else:
                merged[key] = value
        return merged
    
    def is_atom(self, tokens: list[str], i: int) -> bool:
        return i < len(tokens) and re.fullmatch(ATOM_RE, tokens[i]) is not None

    def is_quantifier(self, tokens: list[str], i: int) -> bool:
        return i < len(tokens) and tokens[i].isdigit()

if __name__ == "__main__":
    s = Solution()
    print(s.countOfAtoms("H2O"))
    print(s.countOfAtoms("Mg(OH)29"))
    print(s.countOfAtoms("K4(ON(SO3)2)2"))
