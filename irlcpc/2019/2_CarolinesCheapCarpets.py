from utils import *

D, O, N = nums(input())
# print(D, O, N)

# recursive impl
def iswhite(dim: int, order: int, x: int, y: int) -> bool:
    if order <= 0:
        return False
    # is the point in the middle section?
    if x >= dim // 3 and x < (2 * dim // 3) \
        and y >= dim // 3 and y < (2 * dim // 3):
        return True
    
    return iswhite(dim // 3, order - 1, x % (dim // 3), y % (dim // 3))

# iterative impl
def iw(dim: int, order: int, x: int, y: int) -> bool:
    while order > 0:
        if x >= dim // 3 and x < (2 * dim // 3) \
            and y >= dim // 3 and y < (2 * dim // 3):
            return True
        order -= 1
        x %= dim // 3
        y %= dim // 3
        dim //= 3
    return False

positions: list[list[int]] = []
for _ in range(N):
    positions.append(nums(input()))

dimension = 3 ** D
# ans = []
# cache: dict[list[int], bool] = {}
# for p in positions:
#     if res := cache.get(p):
#         ans.append(res)
#     else:
#         res = iw(dimension, O, p[0], p[1])
#         cache[p] = res
#         ans.append(res)
# ans = list(map(lambda a: "w" if a else "b"))
ans = list(map(lambda a: "w" if a else "b", map(lambda p: iw(dimension, O, p[0], p[1]), positions)))
print(" ".join(ans))