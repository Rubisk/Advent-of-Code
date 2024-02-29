with open("day_6.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()][::-1]

total = 0
while len(lines) > 0:
    fields = set()
    line = lines.pop()
    for c in line:
        fields.add(c)

    while len(lines) > 0 and line != "":
        line = lines.pop()
        if line == "":
            continue
        line_fields = set()
        for c in line:
            line_fields.add(c)
        fields.intersection_update(line_fields)

    count = len(fields)
    total += count

print(total)
