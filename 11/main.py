from tqdm import tqdm
import functools

with open('input') as f:
    stones = list(map(int, f.read().strip().split()))

@functools.cache
def recursiveMaybe(val, tree):
    if tree == 0:
        return 1

    if val == 0:
        return recursiveMaybe(1, tree - 1)
    elif len(s := str(val)) % 2 == 0:
        return recursiveMaybe(int(s[:len(s) // 2]), tree - 1) \
             + recursiveMaybe(int(s[len(s) // 2:]), tree - 1)
    else:
        return recursiveMaybe(val * 2024, tree - 1)


print(f"part 1: {sum([recursiveMaybe(stone, 25) for stone in stones])}")
print(f"part 2: {sum([recursiveMaybe(stone, 75) for stone in stones])}")
