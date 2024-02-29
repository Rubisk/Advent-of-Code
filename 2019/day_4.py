
def generate_numbers(length, start_int, need_adjacent=True, first=True):
    if length == 0:
        if need_adjacent:
            return
        yield 0
        return
    for i in range(start_int, 10):
        if (i == start_int) and not first:
            new_need_adjacent = False
        else:
            new_need_adjacent = need_adjacent
        for tail in generate_numbers(length - 1, i, new_need_adjacent, False):
            yield i * 10 ** (length - 1) + tail


counter = 0
for x in generate_numbers(6, 1):
    if 206938 <= x <= 679128:
        digits = [int(a) for a in str(x)]
        has_valid_double = False
        for j in range(len(digits) - 1):
            if digits[j] == digits[j + 1]:
                if j + 2 < len(digits) and (digits[j] == digits[j + 1] == digits[j + 2]):
                    continue
                elif j > 0 and (digits[j] == digits[j + 1] == digits[j - 1]):
                    continue
                has_valid_double = True
        if has_valid_double:
            print(x, digits)
            counter += 1
print(counter)
