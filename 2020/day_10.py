from functools import wraps


def cache_all(function):
    cache = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            value = function(*args)
            cache[args] = value
            return value
    return wrapper


@cache_all
def count_arrangements(lines_as_tuple):
    if len(lines_as_tuple) == 1:
        return 1

    total = 0
    mutable_lines = list(lines_as_tuple)
    for i in range(1, min(4, len(lines_as_tuple))):
        if lines_as_tuple[i] - lines_as_tuple[0] <= 3:
            total += count_arrangements(tuple(mutable_lines[i:]))
    return total


with open("day_10.txt") as input_file:
    lines = [int(line) for line in input_file.readlines()]


lines = sorted(lines)
lines = [0] + lines + [lines[-1] + 3]


print(count_arrangements(tuple(lines)))
