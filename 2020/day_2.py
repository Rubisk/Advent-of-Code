valid_count = 0


def valid_line(line):
    numbers, letter, password = line.split(" ")
    number1, number2 = map(int, numbers.split("-"))
    letter = letter[0]
    password = password[number1 - 1] + password[number2 - 1]
    count = 0
    for pwd_letter in password:
        if pwd_letter == letter:
            count += 1
    return count == 1


print(valid_line("1-3 a: abcde"))
print(valid_line("1-3 b: cdefg"))
print(valid_line("2-9 c: ccccccccc"))


with open("day_2.txt") as input_file:
    for line in input_file.readlines():
        if valid_line(line):
            valid_count += 1
        else:
            print(line)
print(valid_count)

