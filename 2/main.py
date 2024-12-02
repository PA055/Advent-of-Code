data = []
with open('input') as f:
    for line in f.readlines():
        data.append([int(i) for i in line.split()])


def issafe(lst):
    increments = []
    for i in range(len(lst) - 1):
        increments.append(lst[i + 1] - lst[i])
    return all([-3 <= incr <= -1 for incr in increments]) or all([1 <= incr <= 3 for incr in increments])


safeCount = 0
safeishCount = 0
for line in data:
    if issafe(line):
        print(line)
        safeCount += 1
    if any(issafe(line[:i] + line[i+1:]) for i in range(len(data))):
        print(f'ish: {line}')
        safeishCount += 1

print(f"part 1: {safeCount}")
print(f"part 2: {safeishCount}")
