from utils import *
from collections import deque

N = int(input())
knight_pos = tuple(nums(input()))
king_pos = tuple(nums(input()))
print(knight_pos, king_pos)

def vadd(u: list[int], v: list[int]) -> list[int]:
    s = []
    for i in range(len(u)):
        s.append(u[i] + v[i])
    return s

directions = []
deltas = [-2, -1, 1, 2]
for i in range(4):
    for j in range(4):
        if i != j:
            for di in deltas:
                for dj in deltas:
                    if abs(di) != abs(dj):
                        move = [0, 0, 0, 0]
                        move[i] = di
                        move[j] = dj
                        directions.append(tuple(move))
print()

def bfs(start, target):
    # BFS setup
    queue = deque([(start, 0)])  # (current position, number of moves)
    visited = set()
    visited.add(tuple(start))

    while queue:
        current, moves = queue.popleft()
        if current == target:
            return moves
        for dx1, dx2, dx3, dx4 in directions:
            next_position = (
                current[0] + dx1,
                current[1] + dx2,
                current[2] + dx3,
                current[3] + dx4
            )
            if all(0 <= coord < N for coord in next_position) and tuple(next_position) not in visited:
                visited.add(tuple(next_position))
                queue.append((next_position, moves + 1))
    return -1

print(bfs(knight_pos, king_pos))