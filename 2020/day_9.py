with open("day_9.txt") as input_file:
    lines = [int(line) for line in input_file.readlines()]

print(lines)

CACHE_SIZE = 25
for i in range(CACHE_SIZE, len(lines)):
    invalid_i = True
    for j in range(i - CACHE_SIZE, i):
        for k in range(i - CACHE_SIZE, j):
            if lines[j] + lines[k] == lines[i]:
                invalid_i = False
    if invalid_i:
        invalid_number = lines[i]


lower_bound = 0
upper_bound = 0

while sum(lines[lower_bound:upper_bound]) != invalid_number:
    if sum(lines[lower_bound:upper_bound]) < invalid_number:
        upper_bound += 1
    else:
        lower_bound += 1

print(min(lines[lower_bound:upper_bound]) + max(lines[lower_bound:upper_bound]))
