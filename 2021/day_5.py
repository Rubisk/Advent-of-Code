import itertools as it
from copy import copy

def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    return gcd(b, a % b)
    

with open("day_5_test.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]

lines = [[tuple(int(x) for x in c.split(",")) for c in line.split(" -> ")] for line in lines]
gmin = min(map(min, map(min, lines)))
gmax = max(map(max, map(max, lines)))


def in_line(x, y, line):
    if not (line[0][0] == line[1][0]) or (line[0][1] == line[1][1]):
        return False
    x0 = line[0][0]
    x1 = line[1][0]
    
    y0 = line[0][1]
    y1 = line[1][1]
    
    dx = x0 - x1
    dy = y0 - y1
    
    g = gcd(dx, dy)
    dx = dx / g
    dy = dy / g
    return (x - x0) * dy == (y - y0) * dx
    

for x, y in it.product(range(gmin, gmax + 1), repeat=2):
    if any(in_line(x, y, line) for line in lines):
        print(x, y)



