import itertools

map = []
with open('input') as f:
    for row in f.readlines():
        map.append(list(row.strip()))

mapSize = (len(map), len(map[0]))
antennaPositions = {s: [] for s in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890'}

for y, row in enumerate(map):
    for x, cell in enumerate(row):
        if cell == '.': continue
        antennaPositions[cell].append((y, x))

antinodes = set()
harmonics = set()
for symbol, positions in antennaPositions.items():
    if len(positions) < 2: continue
    # print(symbol)
    for a, b in itertools.combinations(positions, 2):
        harmonics.add(a)
        harmonics.add(b)
        offset = (b[0] - a[0], b[1] - a[1])
        # print(a, b, offset)

        antinodePos1 = (b[0] + offset[0], b[1] + offset[1])
        if 0 <= antinodePos1[0] < len(map) and 0 <= antinodePos1[1] < len(map[0]):
            # print(antinodePos)
            antinodes.add(antinodePos1)

        while 0 <= antinodePos1[0] < len(map) and 0 <= antinodePos1[1] < len(map[0]):
            harmonics.add(antinodePos1)
            antinodePos1 = (antinodePos1[0] + offset[0], antinodePos1[1] + offset[1])

        antinodePos2 = (a[0] - offset[0], a[1] - offset[1])
        if 0 <= antinodePos2[0] < len(map) and 0 <= antinodePos2[1] < len(map[0]):
            # print(antinodePos)
            antinodes.add((antinodePos2[0], antinodePos2[1]))

        while 0 <= antinodePos2[0] < len(map) and 0 <= antinodePos2[1] < len(map[0]):
            harmonics.add(antinodePos2)
            antinodePos2 = (antinodePos2[0] - offset[0], antinodePos2[1] - offset[1])


print(f"part 1: {len(antinodes)}")
print(f"part 2: {len(harmonics)}")
