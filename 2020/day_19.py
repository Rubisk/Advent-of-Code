import itertools as it

with open("day_19.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]


rules = dict()

i = 0
while i < len(lines) and lines[i] != "":
    rule = lines[i]
    rule_id, rule_info = rule.split(": ")
    rule_id = int(rule_id)
    if "\"" in rule_info:
        rule_info = rule_info.split("\"")[-2]
        rules[rule_id] = rule_info
    elif "|" in rule_info:
        left, right = rule_info.split("|")
        left = tuple(int(x) for x in left.split(" ") if len(x) > 0)
        right = tuple(int(x) for x in right.split(" ") if len(x) > 0)
        rules[rule_id] = (left, right)
    else:
        rule = tuple(int(x) for x in rule_info.split(" ") if len(x) > 0)
        rules[rule_id] = (rule, )
    i += 1

i += 1
words = []
while i < len(lines):
    words.append(lines[i])
    i += 1

max_length = max(map(len, words))


patterns = [set() for _ in range(max_length + 1)]

for length in range(1, max_length + 1):
    for word in words:
        i = 0
        while i + length <= len(word):
            patterns[length].add(word[i:i + length])
            i += 1

rule_patterns = dict()
while len(rules) > 0:
    for number, rule in rules.items():
        if type(rule) is str:
            rule_patterns[number] = [rule]
            rules.pop(number)
            break
        else:
            readable = True
            for sub_rule in rule:
                if not all(x in rule_patterns.keys() for x in sub_rule if x != number):
                    readable = False
            if not readable:
                continue
            rule_patterns[number] = set()

            while any(number in sub_rule for sub_rule in rule):

                def find_min_length(proposed_rule):
                    _length = 0
                    for prop in proposed_rule:
                        if number == prop:
                            continue
                        _length += min(map(len, rule_patterns[prop]))
                    return _length

                for sub_rule in rule:
                    if number in sub_rule:
                        index = sub_rule.index(number)
                        for _sub_rule in rule:
                            new_sub_rule = (*sub_rule[:index], *_sub_rule, *sub_rule[index + 1:])
                            if find_min_length(new_sub_rule) < len(patterns) + 1:
                                rule = (*rule, new_sub_rule)
                        rule = tuple(x for x in rule if x != sub_rule)

            for sub_rule in rule:
                sub_patterns = []
                for i in sub_rule:
                    sub_patterns.append(rule_patterns[i])

                while len(sub_patterns) > 1:
                    new_patterns = set()
                    for x in it.product(sub_patterns[0], sub_patterns[1]):
                        mask = "".join(x)
                        if len(mask) < len(patterns) and mask in patterns[len(mask)]:
                            new_patterns.add(mask)
                    sub_patterns = [new_patterns, *sub_patterns[2:]]
                for mask in sub_patterns[0]:
                    rule_patterns[number].add(mask)
            rules.pop(number)
            break
count = 0
for word in words:
    if word in rule_patterns[0]:
        count += 1
print(count)

