import itertools as it

with open("day_1.txt") as input_file:
    numbers = [int(line) for line in input_file.readlines()]

for number1, number2 in it.combinations(numbers, 2):
    if 2020 - number1 - number2 in numbers:
        print(number1 * number2 * (2020 - number1 - number2))


