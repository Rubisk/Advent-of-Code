import copy
import itertools as it

program_input = open("input_13.txt").readline()

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


board = []
program_raw[0] = 2
score = -1

drawings = [" ", "■", "X", "_", "O"]


def joystick():
    yield 0
    while True:
        ball_x = -1
        player_x = -1
        for row in board:
            if 3 in row:
                ball_x = row.index(3)
            if 4 in row:
                player_x = row.index(4)
        if ball_x > player_x:
            yield -1
        elif ball_x < player_x:
            yield 1
        else:
            yield 0


def set_board(x, y, a):
    if x == -1 and y == 0:
        global score
        score = a
        return
    while len(board) <= y:
        board.append([])
    while len(board[y]) <= x:
        board[y].append(0)
    board[y][x] = a

game = int_code(program_raw, joystick())
while True:
    try:
        x = next(game)
        y = next(game)
        t = next(game)
        set_board(x, y, t)
    except StopIteration:
        break


print(score)