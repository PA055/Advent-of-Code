import itertools

garden = []
with open('input') as f:
    for line in f.readlines():
        garden.append(list(line.strip()))


def getInBounds(pos):
    return 0 <= pos[0] < len(garden) and 0 <= pos[1] < len(garden[0])


def floodFill(start, checked=None):
    if checked == None: checked = set() 
    if start in checked:
        return 0, 0, checked, set()
    letter = garden[start[0]][start[1]]
    area = 1
    perimeter = 0
    perimeters = set()
    checked.add(start)

    if getInBounds((start[0] + 1, start[1])) and letter == garden[start[0] + 1][start[1]]:
        a, p, c, s = floodFill((start[0] + 1, start[1]), checked)
        area += a
        perimeter += p
        checked.update(c)
        perimeters.update(s)
    else:
        perimeter += 1
        perimeters.add((*start, "down"))

    if getInBounds((start[0] - 1, start[1])) and letter == garden[start[0] - 1][start[1]]:
        a, p, c, s = floodFill((start[0] - 1, start[1]), checked)
        area += a
        perimeter += p
        checked.update(c)
        perimeters.update(s)
    else:
        perimeter += 1
        perimeters.add((*start, "up"))

    if getInBounds((start[0], start[1] + 1)) and letter == garden[start[0]][start[1] + 1]:
        a, p, c, s = floodFill((start[0], start[1] + 1), checked)
        area += a
        perimeter += p
        checked.update(c)
        perimeters.update(s)
    else:
        perimeter += 1
        perimeters.add((*start, "right"))

    if getInBounds((start[0], start[1] - 1)) and letter == garden[start[0]][start[1] - 1]:
        a, p, c, s = floodFill((start[0], start[1] - 1), checked)
        area += a
        perimeter += p
        checked.update(c)
        perimeters.update(s)
    else:
        perimeter += 1
        perimeters.add((*start, "left"))

    return area, perimeter, checked, perimeters


positions = list(itertools.product(range(len(garden)), range(len(garden[0]))))
regions = []
while positions:
    start = positions[0]
    letter = garden[start[0]][start[1]]
    area, perimeter, region, perimeters = floodFill(start)
    regions.append((letter, area, perimeter, region, perimeters))
    # print(letter, area, perimeter, region, perimeters, sep=' - ')
    # print(letter, '-', area, '*', perimeter, '=', area * perimeter)
    for pos in region:
        positions.remove(pos)

print(f"part 1: {sum(a * p for _, a, p, _, _ in regions)}")

total = 0
for letter, area, _, _, perimeters in regions:
    sides = 0
    p = perimeters.copy()
    while p:
        sides += 1
        pos = p.pop()
        start = pos
        # print(pos)
        while getInBounds(pos):
            if pos[2] in ('up', 'down') and (pos[0], pos[1] + 1, pos[2]) in p:
                pos = (pos[0], pos[1] + 1, pos[2])
                p.remove(pos)
            elif pos[2] in ('left', 'right') and (pos[0] + 1, pos[1], pos[2]) in p:
                pos = (pos[0] + 1, pos[1], pos[2])
                p.remove(pos)
            else:
                break

        pos = start
        while getInBounds(pos):
            if pos[2] in ('left', 'right') and (pos[0] - 1, pos[1], pos[2]) in p:
                pos = (pos[0] - 1, pos[1], pos[2])
                p.remove(pos)
            elif pos[2] in ('up', 'down') and (pos[0], pos[1] - 1, pos[2]) in p:
                pos = (pos[0], pos[1] - 1, pos[2])
                p.remove(pos)
            else:
                break
    # print(letter, area, sides)
    total += area * sides
print(f"part 2: {total}")
