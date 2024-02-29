import copy

SIZE = 12

with open("day_20.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]

tiles = {}
for i in range(int(len(lines) / 12)):
    tile_id = int(lines[12 * i][5:9])
    tile = [list(x) for x in lines[12 * i + 1:12 * i + 11]]
    tiles[tile_id] = tile


def get_sides(tile):
    yield tile[0]
    yield tile[-1]
    yield [tile[x][0] for x in range(10)]
    yield [tile[x][-1] for x in range(10)]
    yield tile[0][::-1]
    yield tile[-1][::-1]
    yield [tile[x][0] for x in range(10)][::-1]
    yield [tile[x][-1] for x in range(10)][::-1]


def print_tile(tile):
    for row in tile:
        print("".join(row))
    print()


def rotate_90(tile):
    tile_size = len(tile)
    return [[tile[tile_size - 1 - j][i] for j in range(tile_size)] for i in range(tile_size)]


def flip(tile):
    tile_size = len(tile)
    return [[tile[i][tile_size - 1 - j] for j in range(tile_size)] for i in range(tile_size)]


def orientations(tile):
    _tile = copy.deepcopy(tile)
    for _ in range(4):
        yield _tile
        _tile = rotate_90(_tile)
    _tile = flip(_tile)
    for _ in range(4):
        yield _tile
        _tile = rotate_90(_tile)


side_counter = {}
for tile in tiles.values():
    for side in get_sides(tile):
        side = tuple(side)
        side_counter[side] = side_counter.get(side, 0) + 1

single_sides = [side for (side, count) in side_counter.items() if count == 1]

corner_tiles = []
for (tile_id, tile) in tiles.items():
    if len([side for side in get_sides(tile) if tuple(side) in single_sides]) == 4:
        corner_tiles.append((tile_id, tile))
assert len(corner_tiles) == 4


tile_grid = [[] for _ in range(12)]
unused_ids = set(tiles.keys())


tile_id, tile = corner_tiles[0]
while tuple(tile[0]) not in single_sides or tuple(tile[i][0] for i in range(10)) not in single_sides:
    tile = rotate_90(tile)
tile_grid[0].append(tile)

unused_ids.remove(tile_id)

for j in range(1, SIZE):
    bottom = tile_grid[j - 1][0][9]
    for tile_id, tile in tiles.items():
        if tile_id not in unused_ids:
            continue
        for orientation in orientations(tile):
            if tuple(orientation[0]) == tuple(bottom):
                tile_grid[j].append(orientation)
                unused_ids.remove(tile_id)

for j in range(SIZE):
    for i in range(1, SIZE):
        right_side = [tile_grid[j][i - 1][k][9] for k in range(10)]
        for tile_id, tile in tiles.items():
            for orientation in orientations(tile):
                if tile_id not in unused_ids:
                    continue
                if tuple([orientation[k][0] for k in range(10)]) == tuple(right_side):
                    tile_grid[j].append(orientation)
                    unused_ids.remove(tile_id)


total_grid = [[tile_grid[int(i / 8)][int(j / 8)][1 + (i % 8)][1 + (j % 8)]
               for j in range(SIZE * 8)] for i in range(SIZE * 8)]


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster = monster.split("\n")
print(monster)


def find_monsters(tile):
    count = 0
    tile_size = len(tile)
    edited_tile = copy.deepcopy(tile)
    for x in range(tile_size - len(monster[0]) + 1):
        for y in range(tile_size - len(monster) + 1):
            valid = True
            for dx in range(len(monster[0])):
                for dy in range(len(monster)):
                    if monster[dy][dx] == "#" and tile[y + dy][x + dx] != "#":
                        valid = False
            if valid:
                for dx in range(len(monster[0])):
                    for dy in range(len(monster)):
                        if monster[dy][dx] == "#":
                            edited_tile[y + dy][x + dx] = "O"
                count += 1
    return count, edited_tile


for (i, orientation) in enumerate(orientations(total_grid)):
    count, edited = find_monsters(orientation)
    if count > 0:
        total = 0
        for line in edited:
            total += len([x for x in line if x == "#"])
        print(total)
