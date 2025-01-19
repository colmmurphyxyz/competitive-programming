import heapq
from math import sqrt
from utils import *

def dist(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sqrt(sum)

N, M, k = nums(input())

planets = []
planet_names = {}

for _ in range(N):
    name, x, y, z = input().split(" ")
    x = float(x)
    y = float(y)
    z = float(z)
    planets.append((name, (x, y, z)))
    planet_names[name] = (x, y, x)

print()

for _ in range(M):
    name = input()
    coords = planet_names[name]
    # smallest_by_key = heapq.nsmallest(2, data, key=lambda x: x[0])
    smallest = heapq.nsmallest(k + 1, planets, key = lambda x: dist(coords, x[1]))
    # print(smallest)
    smallest = list(map(lambda x: x[0], smallest))
    smallest.remove(name)
    print(f"{name}: ", end="")
    print(", ".join(smallest), end="\n")