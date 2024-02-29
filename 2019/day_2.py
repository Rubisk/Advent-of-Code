import copy
import itertools as it


program_input = open("input_2.txt").readline()

program_constant = [int(x) for x in program_input.split(",")]


for (x, y) in it.product(range(len(program_constant)), repeat=2):
    program = copy.copy(program_constant)
    program[1] = x
    program[2] = y

    position = 0
    while program[position] != 99:
        opcode = program[position]
        if opcode not in (1, 2):
            raise Exception("Something went wrong!")
        input_1 = program[program[position + 1]]
        input_2 = program[program[position + 2]]
        if opcode == 1:
            result = input_1 + input_2
        else:  # opcode == 2
            result = input_1 * input_2
        output_position = program[position + 3]
        program[output_position] = result
        position += 4

    if program[0] == 19690720:
        print(100 * x + y)

