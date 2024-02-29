program_input = open("input_8.txt").readline()


def read_image(width, length):
    layers = []
    input_file = open("input_8.txt")
    current_layer = []
    line = input_file.read(width)
    while line:
        current_layer.append([int(x) for x in line])
        if len(current_layer) == length:
            layers.append(current_layer)
            current_layer = []
        line = input_file.read(width)
    input_file.close()
    return layers


def count_pixels(layer, i):
    count = 0
    for row in layer:
        for pixel in row:
            if pixel == i:
                count += 1
    return count


image = read_image(25, 6)

decoded_image = [[0 for _ in range(25)] for __ in range(6)]
for x in range(25):
    for y in range(6):
        depth = 0
        while image[depth][y][x] == 2:
            depth += 1
        decoded_image[y][x] = image[depth][y][x]
for row in decoded_image:
    print("".join(map(lambda t: "0" if t == 1 else " ", row)))

