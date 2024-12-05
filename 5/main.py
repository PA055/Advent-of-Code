rules = []
updates = []
with open('input') as f:
    line = '-'
    while line != '':
        line = f.readline().strip()
        if line == '': break
        rules.append(tuple(map(int, line.split('|'))))
    for line in f.readlines():
        updates.append(list(map(int, line.strip().split(','))))

# print(updates)
# rules.sort(key=lambda x: x[0])
# print(rules)


def getIncorrectRules(update):
    badRules = []
    for i, page in enumerate(update):
        for rule in [r for r in rules if r[0] == page]:
            if rule[1] in update[:i]:
                badRules.append(rule)
    return badRules


total = 0
incorrectUpdates = []
for update in updates:
    validUpdate = True
    for i, page in enumerate(update):
        # print(f"page: {page}")
        for rule in [r for r in rules if r[0] == page]:
            # print(f"rule: {rule}")
            if rule[1] in update[:i]:
                # print(f"invalid: {update} because of rule: {rule}")
                if update not in incorrectUpdates:
                    incorrectUpdates.append(update)
                validUpdate = False
    if validUpdate:
        # print(f"valid: {update}")
        total += update[len(update) // 2]
print(f"part 1: {total}")

for update in incorrectUpdates:
    print('--------------------')
    badRules = getIncorrectRules(update)
    print(update)
    while len(badRules) > 0:
        print('------')
        print(badRules)
        for rule in badRules:
            update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])],  update[update.index(rule[0])]
        badRules = getIncorrectRules(update)
print(f"part 2: {sum([u[len(u) // 2] for u in incorrectUpdates])}")
