from sage.all import Matrix, vector
from sage.modules.free_module_integer import IntegerLattice
import itertools
import re

machines = []
with open('input') as f:
    for A, B, P, *_ in itertools.batched(f.readlines(), 4):
        ax, ay = re.match(r"Button A: X\+(\d+), Y\+(\d+)", A, re.IGNORECASE).groups()
        bx, by = re.match(r"Button B: X\+(\d+), Y\+(\d+)", B, re.IGNORECASE).groups()
        gx, gy = re.match(r"Prize: X=(\d+), Y=(\d+)", P, re.IGNORECASE).groups()
        machines.append(((int(ax), int(ay)), (int(bx), int(by)), (int(gx), int(gy))))


def getSolution(A, B, P):
    M = Matrix([vector(A), vector(B)])
    P = vector(P)
    if P in IntegerLattice(M):
        return tuple(M.solve_left(P))
    return False


tokens = 0
for i, machine in enumerate(machines):
    g = getSolution(*machine)
    if isinstance(g, tuple):
        # print(i, g)
        tokens += int(g[0] * 3 + g[1])
print(f"part 1: {tokens}")

tokens = 0
for i, machine in enumerate(machines):
    m = (machine[0], machine[1], (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000))
    g = getSolution(*m)
    if isinstance(g, tuple):
        # print(i, g)
        tokens += int(g[0] * 3 + g[1])
print(f"part 2: {tokens}")
