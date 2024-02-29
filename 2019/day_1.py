def calculate_fuel(mass):
    fuel = max(int(mass / 3) - 2, 0)
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    return fuel

total = 0
for line in open("input_1.txt").readlines():
    total += calculate_fuel(int(line))
print(total)

