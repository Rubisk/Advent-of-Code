import itertools as it

with open("day_1.txt") as input_file:
    numbers = [int(line) for line in input_file.readlines()]

total = len([(x, y) for (x, y) in zip(numbers, numbers[3:]) if y > x])
print(total)

