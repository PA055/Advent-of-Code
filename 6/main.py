from tqdm import tqdm
from multiprocessing import Pool
import itertools

playerIndex = [-1, -1, '']
map = []
with open('input') as f:
    for x, line in enumerate(f.readlines()):
        map.append(list(line.strip()))
        if '^' in line:
            playerIndex = [x, line.index('^'), 'up']
        if 'v' in line:
            playerIndex = [x, line.index('v'), 'down']
        if '<' in line:
            playerIndex = [x, line.index('<'), 'left']
        if '>' in line:
            playerIndex = [x, line.index('>'), 'right']

original = [line[:] for line in map]
start = playerIndex[:]


def getInBounds(pos):
    return 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])


while getInBounds(playerIndex):
    if playerIndex[2] == 'up':
        if not getInBounds([playerIndex[0] - 1, playerIndex[1]]):
            map[playerIndex[0]][playerIndex[1]] = 'X'
            break
        if map[playerIndex[0] - 1][playerIndex[1]] == '#':
            playerIndex[2] = 'right'
            continue
        map[playerIndex[0]][playerIndex[1]] = 'X'
        playerIndex[0] -= 1

    if playerIndex[2] == 'down':
        if not getInBounds([playerIndex[0] + 1, playerIndex[1]]):
            map[playerIndex[0]][playerIndex[1]] = 'X'
            break
        if map[playerIndex[0] + 1][playerIndex[1]] == '#':
            playerIndex[2] = 'left'
            continue
        map[playerIndex[0]][playerIndex[1]] = 'X'
        playerIndex[0] += 1

    if playerIndex[2] == 'left':
        if not getInBounds([playerIndex[0], playerIndex[1] - 1]):
            map[playerIndex[0]][playerIndex[1]] = 'X'
            break
        if map[playerIndex[0]][playerIndex[1] - 1] == '#':
            playerIndex[2] = 'up'
            continue
        map[playerIndex[0]][playerIndex[1]] = 'X'
        playerIndex[1] -= 1

    if playerIndex[2] == 'right':
        if not getInBounds([playerIndex[0], playerIndex[1] + 1]):
            map[playerIndex[0]][playerIndex[1]] = 'X'
            break
        if map[playerIndex[0]][playerIndex[1] + 1] == '#':
            playerIndex[2] = 'down'
            continue
        map[playerIndex[0]][playerIndex[1]] = 'X'
        playerIndex[1] += 1

print(f"part 1: {sum([1 if c == 'X' else 0 for line in map for c in line])}")


def getIsLoop(pos):
    map = [line[:] for line in original]
    map[pos[0]][pos[1]] = '#'
    playerIndex = start[:]
    posistions = [playerIndex[:]]
    while getInBounds(playerIndex):
        if playerIndex[2] == 'up':
            if not getInBounds([playerIndex[0] - 1, playerIndex[1]]):
                return False
            if map[playerIndex[0] - 1][playerIndex[1]] == '#':
                playerIndex[2] = 'right'
                continue
            playerIndex[0] -= 1

        if playerIndex[2] == 'down':
            if not getInBounds([playerIndex[0] + 1, playerIndex[1]]):
                return False
            if map[playerIndex[0] + 1][playerIndex[1]] == '#':
                playerIndex[2] = 'left'
                continue
            playerIndex[0] += 1

        if playerIndex[2] == 'left':
            if not getInBounds([playerIndex[0], playerIndex[1] - 1]):
                return False
            if map[playerIndex[0]][playerIndex[1] - 1] == '#':
                playerIndex[2] = 'up'
                continue
            playerIndex[1] -= 1

        if playerIndex[2] == 'right':
            if not getInBounds([playerIndex[0], playerIndex[1] + 1]):
                return False
            if map[playerIndex[0]][playerIndex[1] + 1] == '#':
                playerIndex[2] = 'down'
                continue
            playerIndex[1] += 1

        if playerIndex in posistions:
            return True
        posistions.append(playerIndex[:])


with Pool() as p:
    result = list(tqdm(
        p.imap(
            getIsLoop,
            list(itertools.product(range(len(map)), range(len(map[0]))))
        ),
        total=len(map) * len(map[0])
    ))

print(f"part 2: {sum(1 if i else 0 for i in result)}")
