import itertools as it

with open("day_2.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]

h, d = 0, 0
aim = 0
for line  in lines:
    if line != "\n":
        command, i = line.split(" ")
        i = int(i)
        if command == "forward":
            h += i
            d += aim * i
        elif command == "up":
            aim -= i
        elif command == "down":
            aim += i
        else:
            print("ERROR", command, i)
print(h*d)
