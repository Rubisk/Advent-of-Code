import itertools as it
from copy import copy


with open("day_3.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]


def most_common(lines, i):
    z, o = 0, 0
    for line in lines:
        if line[i] == "1":
            o += 1
        else:
            assert line[i] == "0"
            z += 1
    if z > o:
        return "0"
    else:
        return "1"


def least_common(lines, i):
    z, o = 0, 0
    for line in lines:
        if line[i] == "1":
            o += 1
        else:
            assert line[i] == "0"
            z += 1
    if z <= o:
        return "0"
    else:
        return "1"

oxy_lines = copy(lines)
i = 0
while len(oxy_lines) > 1:
    c = most_common(oxy_lines, i)
    oxy_lines = [x for x in oxy_lines if x[i] == c]
    i += 1

oxy = int(oxy_lines[0], 2)
print(oxy)
    
scrub_lines = copy(lines)
i = 0
while len(scrub_lines) > 1:
    c = least_common(scrub_lines, i)
    scrub_lines = [x for x in scrub_lines if x[i] == c]
    i += 1

scrub = int(scrub_lines[0], 2)
print(scrub)

print(oxy * scrub)
    