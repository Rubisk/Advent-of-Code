with open("day_12.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
direction = 0

wx, wy = 10, 1
x, y = 0, 0
for line in lines:
    letter, value = line[0], int(line[1:])
    if letter == "N":
        wy += value
    elif letter == "S":
        wy -= value
    elif letter == "W":
        wx -= value
    elif letter == "E":
        wx += value
    elif letter == "F":
        x += wx * value
        y += wy * value
    elif letter == "R":
        for _ in range(int(value / 90)):
            wy, wx = -wx, wy

    elif letter == "L":
        for _ in range(int(value / 90)):
            wy, wx = wx, -wy
    print(wx, wy, x, y)

print(abs(x) + abs(y))
