import copy
import itertools as it

program_input = open("input_11.txt").readline()

program_raw = [int(s) for s in program_input.split(",")]

class Program(list):
    def __getitem__(self, item):
        assert type(item) is int
        while len(self) <= item:
            self.append(0)
        return list.__getitem__(self, item)

    def __setitem__(self, key, value):
        assert type(key) is int
        while len(self) <= key:
            self.append(0)
        return list.__setitem__(self, key, value)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 2 ** 32 + self.y


directions = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def turn_right(direction):
    return directions[(directions.index(direction) + 1) % 4]


def turn_left(direction):
    return directions[(directions.index(direction) - 1) % 4]


def int_code(program, input_args):
    program = Program(program)
    position = 0
    relative_base = 0
    while program[position] != 99:
        op_code = program[position]
        operation = op_code % 100
        if (operation % 100) not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            raise Exception("Unknown operation: {0}".format(operation))

        if operation in (1, 2, 7, 8):
            para_count = 3
        elif operation in (5, 6):
            para_count = 2
        else:
            para_count = 1

        op_code = int(op_code / 100)
        parameters = []
        for i in range(para_count):
            if op_code % 10 == 1:
                parameters.append(position + i + 1)
            elif op_code % 10 == 2:
                parameters.append(program[position + i + 1] + relative_base)
            else:
                parameters.append(program[position + i + 1])
            op_code = int(op_code / 10)

        if operation == 1:
            program[parameters[2]] = program[parameters[0]] + program[parameters[1]]
        elif operation == 2:
            program[parameters[2]] = program[parameters[0]] * program[parameters[1]]
        elif operation == 3:
            program[parameters[0]] = next(input_args)
        elif operation == 4:
            yield program[parameters[0]]
        elif operation == 5:
            if program[parameters[0]] != 0:
                position = program[parameters[1]]
                continue
        elif operation == 6:
            if program[parameters[0]] == 0:
                position = program[parameters[1]]
                continue
        elif operation == 7:
            if program[parameters[0]] < program[parameters[1]]:
                program[parameters[2]] = 1
            else:
                program[parameters[2]] = 0
        elif operation == 8:
            if program[parameters[0]] == program[parameters[1]]:
                program[parameters[2]] = 1
            else:
                program[parameters[2]] = 0
        elif operation == 9:
            relative_base += program[parameters[0]]

        position += para_count + 1


board = {}
robot_position = Point(0, 0)
robot_direction = Point(0, 1)
board[robot_position] = 1


def get_colour():
    while True:
        yield board.get(robot_position, 0)


robot = int_code(program_raw, get_colour())
while True:
    try:
        colour = next(robot)
        assert colour in (0, 1)
        board[robot_position] = colour
        turn_direction = next(robot)
        assert turn_direction in (0, 1)
        if turn_direction:
            robot_direction = turn_right(robot_direction)
        else:
            robot_direction = turn_left(robot_direction)
        robot_position += robot_direction
    except StopIteration:
        break

min_x = min(point.x for point in board.keys())
max_x = max(point.x for point in board.keys())
min_y = min(point.y for point in board.keys())
max_y = max(point.y for point in board.keys())

for y in range(max_y + 1, min_y - 2, -1):
    row = ""w
    for x in range(min_x - 1, max_x + 1):
        row += " " if board.get(Point(x, y), 0) else "0"
    print(row)

