import re

with open('input') as f:
    data = f.read()

instructions = re.compile(r"mul\((\d+),(\d+)\)")
print(f"part 1: {sum(int(i.group(1)) * int(i.group(2)) for i in instructions.finditer(data))}")

sections = re.split(r'(do\(\))|(don\'t\(\))', data)
consider = True
total = 0
for section in sections:
    if section is None: continue
    if section == 'don\'t()': consider = False
    if section == 'do()': consider = True
    if consider:
        total += sum(int(i.group(1)) * int(i.group(2)) for i in instructions.finditer(section))
print(f"part 2: {total}")

