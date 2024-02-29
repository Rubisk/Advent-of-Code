import copy
import itertools as it


program_input = open("input_5.txt").readline()

program = [int(x) for x in program_input.split(",")]


def intcode(program, input):
    position = 0
    while program[position] != 99:
        op_code = program[position]
        operation = op_code % 100
        if (operation % 100) not in (1, 2, 3, 4, 5, 6, 7, 8):
            raise Exception("Something went wrong!")

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
            else:
                parameters.append(program[position + i + 1])
            op_code = int(op_code / 10)

        if operation == 1:
            program[parameters[2]] = program[parameters[0]] + program[parameters[1]]
        elif operation == 2:
            program[parameters[2]] = program[parameters[0]] * program[parameters[1]]
        elif operation == 3:
            program[parameters[0]] = input
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

        position += para_count + 1


for x in intcode(program, 5):
    print("OUTPUT: {0}".format(x))
