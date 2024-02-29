import copy
import itertools as it


with open("day_17.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]

big_grid_size = len(lines[0]) + 12
small_grid_size = 13


grid = [[[[0 for _ in range(big_grid_size)] for _ in range(big_grid_size)]
         for _ in range(big_grid_size)] for _ in range(big_grid_size)]


for (i, line) in enumerate(lines):
    for (j, value) in enumerate(line):
        grid[6][i + 6][j + 6][6] = (1 if value == "#" else 0)


for i in range(6):
    new_grid = copy.deepcopy(grid)
    for (x, w) in it.product(range(big_grid_size), repeat=2):
        for (y, z) in it.product(range(big_grid_size), repeat=2):
            neighbours = [(x + dx, y + dy, z + dz, w + dw) for (dx, dy, dz, dw) in it.product(range(-1, 2), repeat=4)
                          if ((dx, dy, dz, dw) != (0, 0, 0, 0)) and 0 <= x + dx < big_grid_size
                          and 0 <= y + dy < big_grid_size and 0 <= z + dz < big_grid_size
                          and 0 <= w + dw < big_grid_size]
            active_neighbours = 0
            for c in neighbours:
                if grid[c[0]][c[1]][c[2]][c[3]] == 1:
                    active_neighbours += 1
            if grid[x][y][z][w] == 1:
                if not 2 <= active_neighbours <= 3:
                    new_grid[x][y][z][w] = 0
            else:
                if active_neighbours == 3:
                    new_grid[x][y][z][w] = 1
    grid = copy.deepcopy(new_grid)

total = 0
for (x, y, z, w) in it.product(range(big_grid_size), repeat=4):
    assert grid[x][y][z][w] in (0, 1)
    total += grid[x][y][z][w]
print(total)
