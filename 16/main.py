import copy

map = []
start = tuple()
end = tuple()
with open('test') as f:
    for x, line in enumerate(f.readlines()):
        if 'S' in line:
            start = (x, line.index('S'), 'E')
        if 'E' in line:
            end = (x, line.index('E'))
        line = line.strip().upper().replace('S', '.').replace('E', '.')
        map.append(list(line))


def getInBounds(point):
    return 0 <= point[0] < len(map) and 0 <= point[1] < len(map[1])


def getValue(point):
    if not getInBounds(point):
        return '#'
    return map[point[0]][point[1]]


def bfs(start):
    m = copy.deepcopy(map)
    point = start
    cost = 999999999999999
    frontier = [(start, 0, [])]
    visited = [start[:2]]
    solution = []
    while frontier:
        node = frontier.pop()
        if node[0][:2] == end:
            print(node)
            cost = min(cost, node[1])

        if getValue((node[0][0] + 1, node[0][1])) != '#' and (node[0][0] + 1, node[0][1]) not in visited:
            if node[0][2] == 'S':
                frontier.append(((node[0][0] + 1, node[0][1], 'S'), node[1] + 1, node[2] + [node[0]]))
            else:
                frontier.append(((node[0][0] + 1, node[0][1], 'S'), node[1] + 1001, node[2] + [node[0]]))
            visited.append((node[0][0] + 1, node[0][1]))

        if getValue((node[0][0] - 1, node[0][1])) != '#' and (node[0][0] - 1, node[0][1]) not in visited:
            if node[0][2] == 'N':
                frontier.append(((node[0][0] - 1, node[0][1], 'N'), node[1] + 1, node[2] + [node[0]]))
            else:
                frontier.append(((node[0][0] - 1, node[0][1], 'N'), node[1] + 1001, node[2] + [node[0]]))
            visited.append((node[0][0] - 1, node[0][1]))

        if getValue((node[0][0], node[0][1] + 1)) != '#' and (node[0][0], node[0][1] + 1) not in visited:
            if node[0][2] == 'E':
                frontier.append(((node[0][0], node[0][1] + 1, 'E'), node[1] + 1, node[2] + [node[0]]))
            else:
                frontier.append(((node[0][0], node[0][1] + 1, 'E'), node[1] + 1001, node[2] + [node[0]]))
            visited.append((node[0][0], node[0][1] + 1))

        if getValue((node[0][0], node[0][1] - 1)) != '#' and (node[0][0], node[0][1] - 1) not in visited:
            if node[0][2] == 'W':
                frontier.append(((node[0][0], node[0][1] - 1, 'W'), node[1] + 1, node[2] + [node[0]]))
            else:
                frontier.append(((node[0][0], node[0][1] - 1, 'W'), node[1] + 1001, node[2] + [node[0]]))
            visited.append((node[0][0], node[0][1] - 1))

    return cost

print(bfs(start))
