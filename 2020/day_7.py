with open("day_7.txt") as input_file:
    lines = [line.replace("\n", "").replace("bags", "bag") for line in input_file.readlines()][::-1]

bag_policy = {}

for line in lines:
    outer_bag, inner_bags = line.split(" contain ")
    outer_bag = outer_bag[:-4]

    inner_bag_list = []
    if inner_bags != "no other bag.":
        inner_bags = inner_bags[:-1].split(", ")
        for bag in inner_bags:
            count = int(bag[0])
            type = bag[2:-4]
            inner_bag_list.append((count, type))
    bag_policy[outer_bag] = inner_bag_list


def contains_gold(type):
    if 'shiny gold' in [x[1] for x in bag_policy[type]]:
        return True
    return any([contains_gold(x[1]) for x in bag_policy[type]])


def count_bags(type):
    total = 1
    for (subcount, subtype) in bag_policy[type]:
        total += subcount * count_bags(subtype)
    return total


print(count_bags('shiny gold') - 1)
