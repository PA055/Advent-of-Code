import collections

l1, l2 = [], []
with open("input") as f:
    for line in f.readlines():
        i1, i2 = line.split()
        l1.append(int(i1))
        l2.append(int(i2))

l1.sort()
l2.sort()
print(f"part 1: {sum([abs(i1 - i2) for i1, i2 in zip(l1, l2)])}")

counts = collections.Counter(l2)
sum = 0
for i in l1:
    sum += i * counts[i]
print(f"part 2: {sum}")
