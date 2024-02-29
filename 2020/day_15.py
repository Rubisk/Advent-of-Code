with open("day_15.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]

starting_numbers = [int(x) for x in lines[0].split(",")]

turns_spoken = {n: i for (i, n) in enumerate(starting_numbers)}

goal = 30000000

t = len(starting_numbers)
last_n = starting_numbers[-1]

while t < goal:
    if t % 1000000 == 0:
        print(t)
    result = turns_spoken.get(last_n, 0)
    if result == 0:
        difference = 0
    else:
        difference = t - result - 1
    turns_spoken[last_n] = t - 1
    t += 1
    last_n = difference

print(last_n)
