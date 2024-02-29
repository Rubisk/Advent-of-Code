with open("day_11.txt") as input_file:
    lines = [list(line.replace("\n", "")) for line in input_file.readlines()]

width = len(lines[0])
height = len(lines)


def update_grid(grid):
    new_grid = [["" for _ in range(width)] for __ in range(height)]
    changed = 0

    for x in range(width):
        for y in range(height):
            neighbours = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    i = 1
                    while 0 <= x + i * dx < width and 0 <= y + i * dy < height and \
                            grid[y + i * dy][x + i * dx] == ".":
                        i += 1
                    if 0 <= x + i * dx < width and 0 <= y + i * dy < height:
                        neighbours.append(grid[y + i * dy][x + i * dx])

            occupied_neighbours = len([a for a in neighbours if a == "#"])

            if grid[y][x] == "#" and occupied_neighbours >= 5:
                new_grid[y][x] = "L"
                changed += 1
            elif grid[y][x] == "L" and occupied_neighbours == 0:
                new_grid[y][x] = "#"
                changed += 1
            else:
                new_grid[y][x] = grid[y][x]
    return changed, new_grid


lines_changed = -1

while lines_changed != 0:
    lines_changed, lines = update_grid(lines)
    print("Updated {0} positions.".format(lines_changed))

count = 0
for line in lines:
    count += len([a for a in line if a == "#"])

print(count)
