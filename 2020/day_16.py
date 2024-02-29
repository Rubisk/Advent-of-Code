
class Field(object):

    def __init__(self, name, lower1, upper1, lower2, upper2):
        self._name = name
        self._lower1 = lower1
        self._lower2 = lower2
        self._upper1 = upper1
        self._upper2 = upper2

    def in_range(self, n):
        return (self._lower1 <= n <= self._upper1) or (self._lower2 <= n <= self._upper2)

    def __repr__(self):
        return "{0}".format(self._name)


fields = []
with open("day_16.txt") as input_file:
    lines = list(input_file.readlines())
    for (i, line) in enumerate(lines):
        line = line.replace("\n", "")
        if line == "":
            break
        name, ranges = line.split(": ")
        range_1, range_2 = ranges.split(" or ")
        a, b, c, d = map(int, range_1.split("-") + range_2.split("-"))
        fields.append(Field(name, a, b, c, d))
        print(line)

    my_ticket = map(int, lines[i + 2].split(","))

    other_tickets = [[int(y) for y in x.split(",")] for x in lines[i + 5:len(lines)]]

valid_tickets = []
for ticket in other_tickets:
    if all([any([field.in_range(value) for field in fields]) for value in ticket]):
        valid_tickets.append(ticket)


options = [[field for field in fields] for i in range(len(fields))]


for ticket in valid_tickets:
    for (i, value) in enumerate(ticket):
        for (j, field) in enumerate(options[i]):
            if not field.in_range(value):
                options[i].remove(field)


while any([len(x) > 1 for x in options]):
    for (i, options_i) in enumerate(options):
        if len(options_i) == 1:
            for j in range(len(options)):
                if j != i and options_i[0] in options[j]:
                    options[j].remove(options_i[0])

field_order = [x[0] for x in options]

total = 1
for (i, value) in enumerate(my_ticket):
    if field_order[i]._name[:9] == "departure":
        total *= value
print(total)
