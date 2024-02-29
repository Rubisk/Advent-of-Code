import numpy as np
import copy
import itertools as it
import sys


def apply_pattern(input, pattern):
    total = 0
    for i in input:
        factor = next(pattern)
        total += i * factor
    return abs(total) % 10


def generate_pattern(size):
    skip_first = True
    bases = (0, 1, 0, -1)
    base_index = 0
    while True:
        base = bases[base_index]
        for i in range(size):
            if i == 0 and skip_first:
                skip_first = False
                continue
            yield base
        base_index = (base_index + 1) % 4


def apply_fft(input, repetitions):
    for _ in range(repetitions):
        print("PHASE {0}".format(_))
        for i in range(len(input)):
            print(apply_pattern(input, generate_pattern(i + 1)))
    return input


def str_to_seq(string):
    return [int(x) for x in string]


def sum_partial(input_string):
    output_string = [0]
    for x in input_string[::-1]:
        output_string.append(output_string[-1] + x)
    output_string = output_string[1:]
    return [abs(s) % 10 for s in output_string[::-1]]


start = list(it.chain(*it.repeat(str_to_seq(open("input_16.txt").readline()), 10000)))
offset = int("".join(map(str, start[:7])))
print(offset)
print(offset, len(start))
start = start[offset:]
for _ in range(100):
    print("{0}% complete".format(_))
    start = sum_partial(start)
print(start)
print("".join(map(str, start[:8])))
