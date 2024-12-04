data = []
with open('input') as f:
    for line in f.readlines():
        data.append(list(line.lower().strip()))

lines = []

for row in data:
    lines.append(''.join(row))

for i in range(len(data[0])):
    lines.append(''.join([data[j][i] for j in range(len(data))]))

for i in range(4 - len(data), len(data[0]) - 3):
    lines.append(''.join([data[j][i + j] for j in range(len(data)) if 0 <= i + j <= len(data[0]) - 1]))

for i in range(3, len(data) + len(data[0]) - 4):
    lines.append(''.join([data[i - j][j] for j in range(len(data[0])) if 0 <= i - j <= len(data) - 1]))

xmasCount = 0
for line in lines:
    xmasCount += line.count('xmas')
    xmasCount += line.count('samx')
print(f"part 1: {xmasCount}")

masCount = 0
for y in range(len(data) - 2):
    for x in range(len(data[y]) - 2):
        if data[y + 1][x + 1] != 'a': continue
        if ((data[y + 0][x + 0] == 'm' and data[y + 2][x + 2] == 's') or
                (data[y + 0][x + 0] == 's' and data[y + 2][x + 2] == 'm')) and \
               ((data[y + 2][x + 0] == 'm' and data[y + 0][x + 2] == 's') or
                (data[y + 2][x + 0] == 's' and data[y + 0][x + 2] == 'm')):
            masCount += 1
            print('\n'.join([''.join(line[x:x+3]) for line in data[y:y+3]]))
            print()
print(f"part 2: {masCount}")
