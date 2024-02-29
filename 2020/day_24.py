import copy


with open("day_24.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]


def get_neighbours(tile):
    x, y = tile
    yield (x - 2, y)
    yield (x + 2, y)
    yield (x + 1, y + 1)
    yield (x + 1, y - 1)
    yield (x - 1, y + 1)
    yield (x - 1, y - 1)


def init_tiles(tile_lines):
    flipped_tiles = {}
    for line in tile_lines:
        line = [x for x in line[::-1]]
        x, y = 0, 0
        while len(line) > 0:
            c = line.pop()
            if c == "e":
                x += 2
            elif c == "w":
                x -= 2
            elif c == "n":
                d = line.pop()
                if d == "e":
                    y += 1
                    x += 1
                else:
                    assert d == "w"
                    y += 1
                    x -= 1
            else:
                assert c == "s"
                d = line.pop()
                if d == "e":
                    y -= 1
                    x += 1
                else:
                    assert d == "w"
                    y -= 1
                    x -= 1
        flipped_tiles[(x, y)] = flipped_tiles.get((x, y), 0) + 1
    return flipped_tiles


grid = init_tiles(lines)
for i in range(101):
    print(i, len([x for x in grid.keys() if grid[x] % 2 == 1]))

    new_grid = copy.deepcopy(grid)
    tiles_to_check = set()
    for tile in grid.keys():
        tiles_to_check.add(tile)
        for neighbour in get_neighbours(tile):
            tiles_to_check.add(neighbour)

    for tile in tiles_to_check:
        black_neighbours = []
        for neighbour in get_neighbours(tile):
            if neighbour in grid.keys() and grid[neighbour] % 2 == 1:
                black_neighbours.append(neighbour)
        if tile not in grid.keys() or grid[tile] % 2 == 0:
            if len(black_neighbours) == 2:
                new_grid[tile] = 1
        else:
            assert grid[tile] % 2 == 1
            if len(black_neighbours) not in (1, 2):
                new_grid[tile] = 0
    grid = new_grid
