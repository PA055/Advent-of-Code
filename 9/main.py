fs = ''
with open('test') as f:
    fs = f.read().strip()

uncompressed = []
files = []
spaces = []
pos = 0
for i, char in enumerate(fs):
    if i % 2 == 0:
        files.append((pos, i // 2, int(char)))
        pos += int(char)
        uncompressed.extend([i // 2] * int(char))
    else:
        spaces.append((pos, int(char)))
        pos += int(char)
        uncompressed.extend('.' * int(char))

moved = []
end = len(uncompressed) - 1
for i, char in enumerate(uncompressed):
    if char == '.':
        moved.append(uncompressed[end])
        end -= 1
        while uncompressed[end] == '.':
            end -= 1
    else:
        moved.append(char)

    if i >= end:
        break

checksum = 0
for i, c in enumerate(moved):
    checksum += i * c

# print(fs)
# print(uncompressed)
# print(moved)
print(f"part 1: {checksum}")

part2 = uncompressed[:]
for pos, id, size in files[::-1]:
    for i, (space_pos, space_size) in enumerate(spaces):
        if space_pos < pos and size <= space_size:
            for j in range(size):
                part2[pos + j] = None
                part2[space_pos + j] = id
            spaces[i] = (space_pos + size, space_size - size)

checksum = 0
for i, c in enumerate(moved):
    if c != '.':
        checksum += i * c
print(f"part 2: {checksum}")
