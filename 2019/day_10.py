import copy
import itertools as it


def get_quadrant(x, y):
    if x >= 0 and y > 0:
        return 0
    elif y <= 0 and x > 0:
        return 1
    elif y < 0 and x <= 0:
        return 2
    elif y >= 0 and x < 0:
        return 3
    raise Exception("IMPOSSIBLE")


class Asteroid(object):
    def __init__(self, x_rel, y_rel, layer):
        self.layer = layer
        self.x = x_rel
        self.y = y_rel

    def __cmp__(self, other):
        if self.layer < other.layer:
            return -1
        elif self.layer > other.layer:
            return 1
        quad_self = get_quadrant(self.x, self.y)
        quad_other = get_quadrant(other.x, other.y)
        if quad_self < quad_other:
            return -1
        elif quad_self > quad_other:
            return 1
        else:
            if quad_self == 0:
                val_self = self.x * other.y
                val_other = self.y * other.x
            elif quad_self == 1:
                val_self = -self.y * other.x
                val_other = -other.y * self.x
            elif quad_self == 2:
                val_self = self.x * other.y
                val_other = self.y * other.x
            elif quad_self == 3:
                val_self = -self.y * other.x
                val_other = -other.y * self.x
            else:
                raise Exception("IMPOSSIBLE")
            if val_self < val_other:
                return -1
            elif val_self > val_other:
                return 1
            else:
                return 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __gt__(self, other):
        return self.__cmp__(other) == 1

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

def gcd(a, b):
    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)

    return _gcd(abs(a), abs(b))


grid = []

with open("input_10.txt") as input_file:
    line = input_file.readline()

    while line:
        grid_line = []
        for char in line:
            if char == "\n":
                continue
            assert char in ("#", ".")
            grid_line.append(1 if char == "#" else 0)
        grid.append(grid_line)

        line = input_file.readline()
program_input = open("input_10.txt").readline()

width = len(grid[0])
height = len(grid)


def count_asteroids_between(x, y, ax, ay):
    d = gcd(ax - x, ay - y)
    if d == 0:
        return -1
    small_delta_x = int((ax - x) / d)
    small_delta_y = int((ay - y) / d)
    count = 0
    for i in range(1, d):
        if grid[y + i * small_delta_y][x + i * small_delta_x]:
            count += 1
    return count


def test_asteroid_position(x, y):
    if not grid[y][x]:
        return -1
    count = 0
    for ax in range(width):
        for ay in range(height):
            if grid[ay][ax]:
                if count_asteroids_between(x, y, ax, ay) == 0:
                    count += 1
    return count


def find_best_asteroid():
    best_count = 0
    best_x = -1
    best_y = -1
    for x in range(width):
        for y in range(height):
            count = test_asteroid_position(x, y)
            if best_count < count:
                best_x = x
                best_y = y
                best_count = count
    return best_count, best_x, best_y


_, x, y = find_best_asteroid()

asteroids = []

for ax in range(width):
    for ay in range(height):
        if grid[ay][ax]:
            if x == ax and y == ay:
                continue
            asteroids.append(Asteroid(ax - x, y - ay, count_asteroids_between(x, y, ax, ay)))



i = 200
winner = sorted(asteroids)[i - 1]
print(winner.x + x, y - winner.y)
