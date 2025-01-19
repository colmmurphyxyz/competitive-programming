def preprocess(s: str) -> str:
    sanitised = ""
    for c in s:
        if c not in set(" \t!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~’"):
            sanitised += c
    return sanitised.lower()

N = int(input())
inputs: list[str] = []
for _ in range(N):
    inputs.append(preprocess(input()))

# print()
# for i in inputs:
#     print(i)

def ia(s: str) -> bool:
    odds: set[str] = set()
    for c in s:
        if c in odds:
            odds.remove(c)
        else:
            odds.add(c)

    if len(odds) == 1:
        return len(s) % 2 != 0
    else:
        return len(odds) == 0

def isanadrome(s: str) -> bool:
    occs = {}
    for c in s:
        occs[c] = occs.get(c, 0) + 1
    evens = 0
    odds = 0
    for v in occs.values():
        if v % 2 == 0:
            evens += 1
        else:
            odds += 1

    if odds == 1:
        return len(s) % 2 != 0
    else:
        return odds == 0
    

ans = map(lambda s: ia(s), inputs)
ans = map(lambda a: "1" if a else "0", ans)
print(" ".join(list(ans)))