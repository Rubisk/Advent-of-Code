import copy

with open("day_22.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]


p1_cards = []
p2_cards = []
i = 1
while lines[i] != "":
    p1_cards.append(int(lines[i]))
    i += 1
i += 2
while i < len(lines) and lines[i] != "":
    p2_cards.append(int(lines[i]))
    i += 1


def recursive_combat(p1, p2, depth=0):
    played_games = set()

    while len(p1) > 0 and len(p2) > 0:
        if (tuple(p1), tuple(p2)) in played_games:
            return 0, p1, p2
        played_games.add((tuple(p1), tuple(p2)))
        c1 = p1[0]
        c2 = p2[0]
        if len(p1) > c1 and len(p2) > c2:
            round_winner = recursive_combat(p1[1:c1 + 1], p2[1:c2 + 1], depth=depth + 1)[0]
        else:
            round_winner = 0 if c1 > c2 else 1

        if round_winner == 0:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

        p1 = p1[1:]
        p2 = p2[1:]
    winner = 0 if len(p1) > 0 else 1
    return winner, p1, p2


win, p1_cards, p2_cards = recursive_combat(p1_cards, p2_cards)
if win == 0:
    print(sum((i + 1) * p1_cards[-(i + 1)] for i in range(len(p1_cards))))
else:
    print(sum((i + 1) * p2_cards[-(i + 1)] for i in range(len(p2_cards))))
