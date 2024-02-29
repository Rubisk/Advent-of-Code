with open("day_5.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()][::-1]


def code_to_seat(code):
    row_data = code[:7]
    seat = 0
    for i in range(7):
        if row_data[i] == "B":
            seat += 2 ** (6 - i)

    seat *= 8

    column_data = code[7:10]
    for i in range(3):
        if column_data[i] == "R":
            seat += 2 ** (2 - i)
    return seat


seats = sorted(code_to_seat(line) for line in lines)
start = min(seats)
finish = max(seats)

for i in range(start, finish):
    if i not in seats:
        print(i)
