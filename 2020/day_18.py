import copy
import itertools as it


with open("day_18.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]


def evaluate_expression(expression):
    while "(" in expression:
        if ")" not in expression:
            raise Exception("Unclosed parenthesis")
        end = expression.index(")")
        start = end
        while expression[start] != "(":
            start -= 1
        inner = evaluate_expression(expression[start + 1:end])
        expression = expression[:start] + str(inner) + expression[end + 1:]
    as_list = expression.split(" ")
    i = 0
    while i < len(as_list):
        as_list[i] = int(as_list[i])
        i += 2
    while "+" in as_list:
        i = as_list.index("+")
        value = as_list[i - 1] + as_list[i + 1]
        as_list = [*as_list[:i - 1], value, *as_list[i + 2:]]
    while "*" in as_list:
        i = as_list.index("*")
        value = as_list[i - 1] * as_list[i + 1]
        as_list = [*as_list[:i - 1], value, *as_list[i + 2:]]
    return as_list[0]


print(evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

total = 0
for line in lines:
    total += evaluate_expression(line)
print(total)
