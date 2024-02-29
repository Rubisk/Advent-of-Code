import copy
import itertools as it
from sympy.ntheory.modular import crt


def gcd(list_of_values):
    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)

    d = abs(list_of_values[0])
    for e in list_of_values[1:]:
        d = _gcd(d, abs(e))

    return d


def kgv(list_of_values):
    k = list_of_values[0]
    for e in list_of_values[1:]:
        k = k * e / gcd([k, e])
    return k


class Planet(object):
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def __repr__(self):
        return "pos=<x={0}, y={1}, z={2}>, vel=<x={3}, y={4}, z={5}>".format(*(self.position + self.velocity))

    def apply_gravity(self, other):
        for i in range(3):
            if self.position[i] < other.position[i]:
                self.velocity[i] += 1
            elif self.position[i] > other.position[i]:
                self.velocity[i] -= 1

    def update_position(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def calculate_energy(self):
        return sum(map(abs, self.position)) * sum(map(abs, self.velocity))


def hash_state(state, coordinate):
    hash = 0
    for planet in state:
        value = planet.position[coordinate]
        value += 2 ** 16
        if not 0 <= value < 2 ** 32:
            raise OverflowError
        hash += value
        hash <<= 16

        value = planet.velocity[coordinate]
        if value >= 2 ** 32:
            raise OverflowError
        hash += value
        hash <<= 32
    return hash


def find_repetition(coordinate):
    planets = []

    with open("input_12.txt") as file:
        for line in file.readlines():
            px, py, pz = map(int, line.split(",")[:3])
            planets.append(Planet(px, py, pz))

    hash = hash_state(planets, coordinate)
    hash_table = {}
    t = 0
    while hash not in hash_table.keys():
        hash_table[hash] = t
        t += 1
        for p, q in it.permutations(planets, 2):
            p.apply_gravity(q)
        for p in planets:
            p.update_position()
        hash = hash_state(planets, coordinate)

    return hash_table[hash], t - hash_table[hash]

moduli = []
values = []
for i in range(3):
    v, m = find_repetition(i)
    print(v, m)
    moduli.append(m)
    values.append(v % m)

print(kgv(moduli) + max(values))
