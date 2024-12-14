import collections
import itertools
import re

guards = []
# mapSize = (11, 7)
mapSize = (101, 103)
with open('input') as f:
    for line in f.readlines():
        guards.append(tuple(itertools.batched(map(
            int, re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()
        ), 2)))

nextGuards = guards[:]
# print(nextGuards)
for j in range(100):
    for i, ((x, y), (vx, vy)) in enumerate(nextGuards):
        # print(f"({x}, {y}) + ({vx}, {vy}) = ({x + vx}, {y + vy}) % {mapSize} = ({(x + vx) % mapSize[0]}, {(y + vy) % mapSize[1]})")
        nextGuards[i] = (
            (
                (x + vx) % mapSize[0],
                (y + vy) % mapSize[1]
            ),
            (vx, vy)
        )
    # print(nextGuards)
# print([g[0] for g in nextGuards])
Q1 = [g[0] for g in nextGuards if g[0][0] < mapSize[0] // 2 and g[0][1] < mapSize[1] // 2]
Q2 = [g[0] for g in nextGuards if g[0][0] < mapSize[0] // 2 and g[0][1] > mapSize[1] // 2]
Q3 = [g[0] for g in nextGuards if g[0][0] > mapSize[0] // 2 and g[0][1] < mapSize[1] // 2]
Q4 = [g[0] for g in nextGuards if g[0][0] > mapSize[0] // 2 and g[0][1] > mapSize[1] // 2]
print(f"part 1: {len(Q1) * len(Q2) * len(Q3) * len(Q4)}")

nextGuards = guards[:]
iteration = 0
while True:
    for i, ((x, y), (vx, vy)) in enumerate(nextGuards):
        # print(f"({x}, {y}) + ({vx}, {vy}) = ({x + vx}, {y + vy}) % {mapSize} = ({(x + vx) % mapSize[0]}, {(y + vy) % mapSize[1]})")
        nextGuards[i] = (
            (
                (x + vx) % mapSize[0],
                (y + vy) % mapSize[1]
            ),
            (vx, vy)
        )
    iteration += 1
    positions = collections.Counter(g[0] for g in nextGuards)
    for j in range(mapSize[1]):
        for i in range(mapSize[0]):
            if positions[(i, j)] > 0:
                print('@', end='')
            else:
                print(' ', end='')
        print()
    print(str(iteration) + '-' * 50)

# for part 2 run `python main.py | grep -C 103 "@@@@@@@@"` which
# gets an iteration or 3 with 8 robots in a row which should only
# be the image
