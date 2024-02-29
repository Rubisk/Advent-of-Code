import itertools as it
from copy import copy


with open("day_4_test.txt") as input_file:
    lines = [line.replace("\n", "") for line in input_file.readlines()]


balls = [int(x) for x in lines[0].split(",")]

card_lines = lines[2:]
cards = []
card = []
for line in card_lines:
    if line == "":
        cards.append(card)
        card = []
        continue
    
    card.append([int(x) for x in line.split(" ") if x != ""])

cards.append(card)


def has_bingo(card, numbers):
    for i in range(5):
        if all([card[i][j] in numbers for j in range(5)]):
            return True
        if all([card[j][i] in numbers for j in range(5)]):
            return True
    return False

for n in range(len(balls)):
    no_bingos = []
    for card in cards:
        
        if has_bingo(card, balls[:n + 1]) and len(cards) == 1:
            score = 0
            for i, j in it.product(range(5), repeat = 2):
                if card[i][j] not in balls[:n + 1]:
                    score += card[i][j]
            score *= balls[n]
            print(score)
        elif not has_bingo(card, balls[:n + 1]):
            no_bingos.append(card)
    cards  = no_bingos
        