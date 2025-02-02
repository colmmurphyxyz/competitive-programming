from utils import *

N = int(input())
knight_pos = tuple(nums(input()))
king_pos = tuple(nums(input()))

# generate possible moves
directions = set()
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
                        directions.add(tuple(move))

def manhattan_dist(u, v):
    dist = 0
    for i, j in zip(u, v):
        dist += abs(i - j)
    return dist

def dfs(start, target):
    # BFS setup
    stack = [(start, 0)]  # (current position, number of moves)
    visited = set()
    visited.add(tuple(start))

    while stack:
        current, moves = stack.pop()
        if current == target:
            return moves
        current_dist = manhattan_dist(target, current)
        next_moves = []
        for dx1, dx2, dx3, dx4 in directions:
            next_position = (
                current[0] + dx1,
                current[1] + dx2,
                current[2] + dx3,
                current[3] + dx4
            )
            if all(0 <= coord < N for coord in next_position) and tuple(next_position) not in visited:
                if (d := manhattan_dist(next_position, target)) > current_dist:
                    continue
                # use pre-computed distance to sort 
                next_moves.append((next_position, d))
        # add moves to stack, in order of distance to target
        # positions that are closer to target will be placed at top of stack
        next_moves = sorted(next_moves, key=lambda p: -p[1])
        for m, _ in next_moves:
            visited.add(tuple(m))
            stack.append((m, moves + 1))
    return -1

print(dfs(knight_pos, king_pos))