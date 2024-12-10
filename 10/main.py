topologicalMap = []
with open('input') as f:
    for line in f.readlines():
        topologicalMap.append(list(map(int, line.strip())))


def getInBounds(point):
    return 0 <= point[0] < len(topologicalMap) and 0 <= point[1] < len(topologicalMap[0])


def getPossibleTrails(start, unique):
    if topologicalMap[start[0]][start[1]] == 9:
        if unique:
            return set([start])
        return [start]

    if unique: totalTrails = set()
    else: totalTrails = []
    for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        point = (start[0] + offset[0], start[1] + offset[1])
        if getInBounds(point) and topologicalMap[start[0]][start[1]] + 1 == topologicalMap[point[0]][point[1]]:
            if unique:
                totalTrails.update(getPossibleTrails(point, unique))
            else:
                totalTrails.extend(getPossibleTrails(point, unique))
    return totalTrails


totalTrails = 0
totalScore = 0
for x, line in enumerate(topologicalMap):
    for y, char in enumerate(line):
        if char == 0:
            totalTrails += len(getPossibleTrails((x, y), True))
            totalScore += len(getPossibleTrails((x, y), False))

print(f"part 1: {totalTrails}")
print(f"part 2: {totalScore}")
