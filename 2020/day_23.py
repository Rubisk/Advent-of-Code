class Cup(object):
    next_cup = None

    def __init__(self, n):
        self.n = n


MAX = 1000000

input_string = "712643589"
start = [int(x) for x in input_string]

cups = [Cup(x) for x in range(0, MAX + 1)]

for i in range(len(input_string)):
    cups[start[i]].next_cup = cups[start[(i + 1) % len(input_string)]]

cups[start[-1]].next_cup = cups[10]
for i in range(len(input_string) + 1, MAX):
    cups[i].next_cup = cups[i + 1]
cups[-1].next_cup = cups[start[0]]

current_cup = cups[start[0]]
for _ in range(10000000):

    cup1 = current_cup.next_cup
    cup2 = cup1.next_cup
    cup3 = cup2.next_cup

    current_cup.next_cup = cup3.next_cup
    destination_cup_n = current_cup.n - 1
    while destination_cup_n < 1 or destination_cup_n in [cup1.n, cup2.n, cup3.n]:
        if destination_cup_n < 1:
            destination_cup_n = MAX
        else:
            destination_cup_n -= 1
    destination_cup = cups[destination_cup_n]
    cup3.next_cup = destination_cup.next_cup
    destination_cup.next_cup = cup1
    current_cup = current_cup.next_cup

print(cups[1].next_cup.n * cups[1].next_cup.next_cup.n)
