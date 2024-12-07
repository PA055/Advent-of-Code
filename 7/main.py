from tqdm import tqdm

tests = []
with open('input') as f:
    for line in f.readlines():
        tests.append((int(line.split(':')[0]), [int(i) for i in line.split(':')[1].strip().split()]))


def validateTestPt1(test):
    for i in range(2 ** len(test[1])):
        value = test[1][0]
        for j in range(len(test[1]) - 1):
            if i >> j & 1:
                value += test[1][j + 1]
            else:
                value *= test[1][j + 1]
        if value == test[0]:
            # print(test)
            # print(bin(i)[2:])
            return True
    return False


def validateTestPt2(test):
    for i in range(3 ** len(test[1])):
        value = test[1][0]
        for j in range(len(test[1]) - 1):
            if (i // (3 ** j)) % 3 == 0:
                value += test[1][j + 1]
            elif (i // (3 ** j)) % 3 == 1:
                value *= test[1][j + 1]
            else:
                value = int(f"{value}{test[1][j + 1]}")
        if value == test[0]:
            # print(test)
            # print(bin(i)[2:])
            return True
    return False


total = 0
for test in tqdm(tests):
    if validateTestPt1(test):
        total += test[0]

print(f"part 1: {total}")

total = 0
for test in tqdm(tests):
    if validateTestPt2(test):
        total += test[0]

print(f"part 2: {total}")
