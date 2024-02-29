with open("day_4.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()][::-1]


def find_fields(line):
    return [field.split(":") for field in line.split(" ")]

valid_count = 0


while len(lines) > 0:
    fields = []
    line = lines.pop()
    fields.extend(find_fields(line))

    while len(lines) > 0 and line != "":
        line = lines.pop()
        fields.extend(find_fields(line))

    if [""] in fields:
        fields.remove([""])

    data = {field[0]: field[1] for field in fields}
    fields = data.keys()

    if not ( len(fields) == 8 or (len(fields) == 7 and "cid" not in fields)):
        continue
    if not 1920 <= int(data["byr"]) <= 2002:
        continue
    if not 2010 <= int(data["iyr"]) <= 2020:
        continue
    if not 2020 <= int(data["eyr"]) <= 2030:
        continue
    hgt = data["hgt"]
    if not ((hgt[-2:] == "in" and (59 <= int(hgt[:-2]) <= 76)) or
            (hgt[-2:] == "cm" and (150 <= int(hgt[:-2]) <= 193))):
        continue

    hcl = data["hcl"]
    if not hcl[0] == "#":
        continue
    bad_hc = False
    for i in range(1, 7):
        if not hcl[i] in "0123456789abcdef":
            bad_hc = True
    if bad_hc:
        continue

    if not data["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    if not (len(data["pid"]) == 9 and all([x in "0123456789" for x in data["pid"]])):
        continue

    valid_count += 1

print(valid_count)
