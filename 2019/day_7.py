import copy
import itertools as it

program_input = open("input_7.txt").readline()

program_raw = [int(x) for x in program_input.split(",")]


def int_code(program, input_args):
    position = 0
    while program[position] != 99:
        op_code = program[position]
        operation = op_code % 100
        if (operation % 100) not in (1, 2, 3, 4, 5, 6, 7, 8):
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
            else:
                parameters.append(program[position + i + 1])
            op_code = int(op_code / 10)

        if operation == 1:
            program[parameters[2]] = program[parameters[0]] + program[parameters[1]]
        elif operation == 2:
            program[parameters[2]] = program[parameters[0]] * program[parameters[1]]
        elif operation == 3:
            program[parameters[0]] = input_args.pop(0)
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


def try_combination(program, phase_setting):
    amplifiers = []
    inputs = []
    output = 0
    for phase in phase_setting:
        new_inputs = [phase, output]
        new_amplifier = int_code(copy.copy(program), new_inputs)
        inputs.append(new_inputs)
        amplifiers.append(new_amplifier)
        output = next(new_amplifier)

    while True:
        try:
            inputs[i].append(output)
            output = next(amplifiers[i])
            i = (i + 1) % 5
        except StopIteration:
            break
    return output


best = 0
for perm in it.permutations(range(5, 10)):
    best = max(best, try_combination(program_raw, perm))
print(best)
