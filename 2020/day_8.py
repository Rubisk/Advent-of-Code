with open("day_8.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]

instructions = []
for line in lines:
    operation, argument = line.split(" ")
    argument = int(argument)
    instructions.append([operation, argument])


def run_instructions(_instructions):
    pointer = 0
    _accumulator = 0
    _looped = False

    pointers_seen = []
    while True:
        if pointer in pointers_seen:
            _looped = True
            break
        elif pointer >= len(_instructions):
            break

        _operation, _argument = _instructions[pointer]
        pointers_seen.append(pointer)
        if _operation == "acc":
            _accumulator += _argument
            pointer += 1
        elif _operation == "nop":
            pointer += 1
            continue
        elif _operation == "jmp":
            pointer += _argument

    return _looped, _accumulator


for i in range(len(instructions)):
    if instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
        looped, accumulator = run_instructions(instructions)
        if not looped:
            print(accumulator)
        instructions[i][0] = "nop"
    elif instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
        looped, accumulator = run_instructions(instructions)
        if not looped:
            print(accumulator)
        instructions[i][0] = "jmp"
