with open("day_13.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]


def mod_inv_bruteforce(x, y):
    for z in range(y):
        if (z * x) % y == 1:
            return z


def solve_crt(residue_list):
    if len(residue_list) == 1:
        return residue_list[0][0] % residue_list[0][1]
    else:
        a, m = residue_list[0]
        b, n = residue_list[1]

    c = mod_inv_bruteforce(m, n) * (b - a)
    x = a + c * m
    y = m * n
    return solve_crt([(x, y)] + residue_list[2:])


bus_times = lines[1].split(",")

goal_residues = []
for i, bus in enumerate(bus_times):
    if bus != "x":
        bus = int(bus)
        goal_residues.append([((-i) % bus), bus])

print(solve_crt(goal_residues))


