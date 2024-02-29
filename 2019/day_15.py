import copy
import itertools as it
import sys

sys.setrecursionlimit(10000)

program_input = open("input_15.txt").readline()

program_raw = [int(s) for s in program_input.split(",")]


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
    raise Exception("ROBOT CRASHED")

directions = [Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)]


class Robot(object):

    def __init__(self, code):
        self._input_args = []
        self._program = int_code(code, self.input_gen())
        self.position = Point(0, 0)
        self.memory = {self.position: 0}

    def move(self, direction):
        self._input_args.append(direction + 1)
        output = next(self._program)
        improved = False
        if output != 0:
            old_time = self.memory[self.position]
            self.position += directions[direction]
            current_time = self.memory.get(self.position, -1)
            if current_time == -1 or current_time > old_time + 1:
                if current_time > old_time + 1:
                    print("WE IMPROVED", self.position)
                improved = True
                self.memory[self.position] = old_time + 1
        return output, improved

    def input_gen(self):
        while True:
            yield self._input_args[0]
            self._input_args = self._input_args[1:]

    def try_walk_board(self):
        for direction in range(4):
            output, improved = self.move(direction)
            if output == 0:
                continue
            if improved:   # Move back if we already were at that point in a faster way
                self.try_walk_board()
            if output == 2:
                print("REACHED END IN {0} steps".format(self.memory[self.position]))
                print(self.position)
            if direction in (0, 2):
                self.move(direction + 1)
            else:
                self.move((direction - 1) % 4)

    def walk_to_oxygen(self):
        try:
            for direction in range(4):
                output, improved = self.move(direction)
                if output == 0:
                    continue
                if improved:   # Move back if we already were at that point in a faster way
                    self.walk_to_oxygen()
                if output == 2:
                    self.memory = {self.position: 0}
                    raise OverflowError
                if direction in (0, 2):
                    self.move(direction + 1)
                else:
                    self.move((direction - 1) % 4)
        except OverflowError:
            return

robot = Robot(program_raw)
robot.walk_to_oxygen()
robot.try_walk_board()
print(max(robot.memory.values()))